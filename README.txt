Some considerations for the app:

I'd go with FastAPI for perf reasons but mostly for handling everything error / REST stuff automatically.
For proof of concepts I'm more comfortable with Flask but FastAPI seems to have evolved to similar simplicity

Chose pip + requirements.txt for simplicity, but I will obviously go with any build stack already available
Using poetry only for elementary versioning (patch), but I understand it can be used for deps as well

I will place this directly in master for simplicity, but the simplest I've seen is to keep a development branch
and merge stable stuff to master through pull requests when ready / needs build + release.
Next simplest is to have deployment branches for staging / prod, and merge to those through pull requests
while keeping master fully automated: build + deploy to dev env
Dev culture varies so much across organizations that I became un-opinionated on this and just make recommendations
based on personal experience when needed.



