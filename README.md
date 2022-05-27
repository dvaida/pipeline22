## Some considerations for the implementation:

### Development / Python

I went with FastAPI for perf reasons but mostly for handling everything error / REST stuff automatically.
For proof of concepts I'm more comfortable with Flask but FastAPI seems to have evolved to similar simplicity.

Chose pip + requirements.txt for simplicity, but I will obviously go with any build stack already available
Using poetry only for elementary versioning (patch), but I understand it can be used for deps as well

For code /repo configuration I have chosen to code / deploy from master for simplicity, but the simplest I've
seen / done is to keep a development branch and merge stable stuff to master through pull requests when ready / needs
build + release.

Next simplest is to have deployment branches for staging / prod, and merge to those through pull requests
while keeping master fully automated: build + deploy to dev env
Dev culture varies so much across organizations that I became un-opinionated on this and just make recommendations
based on personal experience when needed.

I've used poetry to version bump and a small shell script to replace the image version in the generated
deployment artefacts (further to be merged by kustomize)

I've chosen to build a Docker image and configure it through ENV vars, but there's more to a 12 factor app. Still,
it's a start.

### Delivery / Deployment

I've chosen the Kubernetes deployment artefacts to be in the same repo as the code instead of separate repos.
It all depends on preferences and team's DevOps culture, I've seen both, developers with strong ownership and who
want to retain / control prod operations / monitoring will prefer all artefacts in the same repo. Teams with centralized
release/deployment and separate / independent platform team will prefer to own deployments and have control over
deployment pace / lifecycle

The eternally hacky way of automatic version bump + commit by the CI is implemented here with minimal care for conflicts:
The kubernetes/deploy folder should *never* be changed by developers, it's generated. Everything outside it is considered
source

CI is implemented with (initially I used Bitbucket - see bitbucket-pipelines.yml, then my free build time expired and
decided to go for Github Actions - see .github/workflow/main.yaml) minimal scripting triggered by commit/pull request.
It is neither safe nor flexible enough, and I am new to kustomize so most probably this can be done way better.
In prod it depends on the env. Github folks tend to prefer CicleCI, on premises deployments - Jenkins, a good chunk of
developers will go with the cloud provider's hosted service.

CD is implemented with ArgoCD which is reading / polling (3 mins intervals) the Bitbucket / Github repo, but obviously
a more timely deployment style would use webhooks.

Also, in prod we'd probably need better flexibility with deployment environments, release / version management and
triggering.

Here I've implemented a trivial continuous delivery + deployment model with each commit to master
bumping the version (patch), building, testing and releasing a docker image on Docker Hub, and automated deployment in a
dev environment through ArgoCD. The way ArgoCD implements gitops safeguards against "no op" deployments. It'll deploy
only when the generated Kubernetes artefacts have changed against production, ignoring other code changes / commits
to the repo.

However, in prod we'd probably want to parametrize more environments (e.g. master/main branch deploys to dev,
staging branch deploys to staging and production branch deploys to production), adding pull requests and reviews
into the mix; and versioning - ability to provide the entire version or specify minor / major bump besides patch.

### Other important things to look into

 * Liveness / readiness probes
 * Metrics / observability
 * Resource limits (rather set cluster wide unusably small limits to force pods to specify their resources)
 * Supply chain security (Docker image scan at build time + image origin at Kubernetes deploy time)
 * Network policies to restrict communication to a minimum even within the cluster

