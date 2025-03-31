# Vercel

You can host the API as a serverless function on Vercel

## Register at Vercel

[Sign-Up](https://vercel.com/signup) and create a "Hobby" account - it's free.

## Install Vercel CLI

```shell
pnpm i -g vercel
```

Note:
1. If `pnpm` is not available because you did not run `./install.sh`,
you can install it manually with `brew install pnpm`.

## Generate Vercel Distribution

```shell
make dist_vercel
```

Notes:
1. Builds and outputs a wheel of the project into vercel_dist/wheels/
2. Generates a vercel_dist/requirements.txt from pyproject.toml including a reference to the wheel.


## Link with Vercel project

```shell
vercel link --cwd dist_vercel --project oe-python-template-example --yes
```

Notes:
1. Creates the Vercel project if not yet existing.
2. Links the dist_vercel/ directory with that project

## Run function locally

```shell
vercel dev --cwd dist_vercel
```

Notes:
1. Runs a local server on port 3000

## Deploy distribution to production on Vercel

```shell
vercel deploy --cwd dist_vercel --archive=tgz --prod
```

Visit the [production deployment](https://oe-python-template-example.vercel.app/)

## Wire Vercel with GitHub for Continuous Deployment

1. Show organisation and project id by executing `cat dist_vercel/.vercel/project.json`
2. [Create secret](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/settings/secrets/actions/new) called `VERCEL_PROJECT_ID` with the
value of `projectId` from step 1
3. [Create secret](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/settings/secrets/actions/new) called `VERCEL_ORG_ID` with the value
of `orgId` from step 1
4. Goto [Vercel Account Settings](https://vercel.com/account/settings/tokens) and create a new token with project scope,
copy the token to clipboard.
5. [Create secret](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/settings/secrets/actions/new) called `VERCEL_TOKEN` with the value
of `projectId` from the previous command
6. [Generate GitHub Personal Access Token](https://github.com/settings/tokens) with Deployments (Read and Write) and
Pull Requests (Read and Write) permissions scoped for repository of the project. Copy the token in your buffer
7. [Create secret](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/settings/secrets/actions/new) called `GH_PATH` with the value
set to the token created in step 6

That's it. The rest is automatic, deploy happening on build of main.
