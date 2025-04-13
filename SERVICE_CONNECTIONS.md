# Setup service connections

## Reporting code coverage via CodeCov (codecov.io)

1. Sign-Up at https://app.codecov.io/
2. Configure via https://app.codecov.io/gh/helmut-hoffer-von-ankershoffen
3. Select (o) Repository token. Copy value of `CODECOV_TOKEN` into your clipboard
4. Goto https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/settings/secrets/actions/new and create a new repository secret called `CODECOV_TOKEN`, pasting the token from your clipboard as value
5. Re-run the `CI / test` GitHub job in case you tried before and it failed as Codecov was not yet wired up

## Analyzing code quality and security analysis via SonarQube cloud (sonarcloud.io)

1. Sign-Up at https://sonarcloud.io
2. Grant access to your new repo via https://github.com/settings/installations -> Configure
3. Goto https://sonarcloud.io/projects/create and select the repo
4. Select Previous Code when prompted
5. Configure by going to https://sonarcloud.io/project/configuration?id=helmut-hoffer-von-ankershoffen_oe-python-template-example and clicking on "With GitHub Actions". Copy the value of `SONAR_TOKEN` into your clipboard.
6. Goto https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/settings/secrets/actions/new and create a new repository secret called `SONAR_TOKEN`, pasting the token from your clipboard as the value
7. Goto https://sonarcloud.io/project/settings?id=helmut-hoffer-von-ankershoffen_oe-python-template-example and select "Quality Gate" in the left menu. Select "Sonar way" as default quality gate.
8. Re-run the `CI / test` GitHub job in case you tried before and it failed as SonarQube was not yet wired up

## Generating and publishing documentation via ReadTheDocs (readthedocs.org)

1. Sign-Up at https://readthedocs.org/
2. Goto https://app.readthedocs.org/dashboard/import/ and search for your repo by enterin oe-python-template-example in the search bar
3. Select the repo and click Continue, then Next.
4. On https://app.readthedocs.org/projects/oe-python-template-example/ wait for the build of the documentation to finish
5. Goto https://oe-python-template-example.readthedocs.io/en/latest/

## Automatic dependency updates via Rennovate (https://github.com/apps/renovate)

1. Goto https://github.com/apps/renovate and click the "Configure" button
2. Select the owner of your project's repository and configure "Repository access"
3. Rennovate creates a [Dependency Dashboard](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/issues?q=is%3Aissue%20state%3Aopen%20Dependency%20Dashboard) as an issue in your repository

## Publishing package to Python Package Index (pypi.org)

1. Execute `uv build`. This will generate the build files (wheel and tar.gz) in the `dist` folder
2. Sign-Up at https://pypi.org/
3. Goto https://pypi.org/manage/account/ and create an API token of scope "Entire account", calling it oe-python-template-example. Copy the value of the token into your clipboard.
4. Execute `uv publish`, entering __token__ as username and paste the token from your clipboard as password. This will register your package on PyPI and upload the build files
5. Goto https://pypi.org/manage/account/ again and delete the previously created token oe-python-template-example of scope "Entire account".
6. Now create an new API token, again called oe-python-template-example, but this time of scope "Project: oe-python-template-example". Copy the token into your clipboard.
7. Goto https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/settings/secrets/actions/new and delete the previously created token.
8. Then create a new repository secret called `UV_PUBLISH_TOKEN`, pasting the token from your clipboard as value
9. In case your `CI / test` job passed, and you are ready to release and publish, bump the version of your project by executing `bump`. In case you tried before completing this setup script, you can as well go to https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/actions/workflows/package-build-publish-release.yml, click on the failed job, and re-run.

## Publishing Docker images to Docker Hub (docker.io)

1. Sign-Up at https://hub.docker.com/
2. Click on your avatar or profile pic and copy the username below that into your clipboard.
3. Goto https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/settings/secrets/actions/new and create a new repository secret called `DOCKER_USERNAME`, setting your username at Docker Hub as the value
4. Goto https://app.docker.com/settings/personal-access-tokens/create and create a new access token setting the description to oe-python-template-example, permissions Read & Write & Delete. Copy the value of the token into your clipboard.
5. Goto https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/settings/secrets/actions/new and create a new repository secret called `DOCKER_PASSWORD`, pasting the token from your clipboard as the value
6. In case your `CI / test` job passed, and you are ready to release and publish, bump the version of your project by executing `bump`. In case you tried before completing this setup script, you can as well go to https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/actions/workflows/package-build-publish-release.yml, click on the failed job, and re-run.

## Publishing Docker images to GitHub Container Registry (ghcr.io)

1. This just works, no further setup required.
2. Just `bump` to release and publish.

## Streamlit app (streamlit.io)

1. Sign-up at https://streamlit.io
2. In settings connect your GitHub account
3. Goto https://share.streamlit.io/new and click "Deploy a public app from GitHub"
4. Select the oe-python-template-example repo, for "Main file path" select `examples/streamlit.py`, for App URL enter `oe-python-template-example`.streamlit.app. Click "Deploy"
5. Goto https://oe-python-template-example.streamlit.app

## GitHub repository settings

1. Goto https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/settings/security_analysis
2. Enable Private vulnerability reporting
3. Enable Dependabot alerts
4. Enable Dependabot security updates
5. CodeQL analyis will be automatically set up via a GitHub action


## Error monitoring and profiling with Sentry

1. Goto https://sentry.io/ and sign-in - it's free for solo devs
2. Follow the instructions to create a new project and get the DSN. Copy the
   value of the token into your clipboard.
3. For your local environment: Open your local `.env` file and set the
   `OE_PYTHON_TEMPLATE_EXAMPLE_SENTRY_DSN` variable to the value of the token from your
   clipboard. You can check `.env.example` for the correct format.
4. For the test, preview and production stage: Goto
   https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/settings/secrets/actions/new
   and create a new repository secret called `OE_PYTHON_TEMPLATE_EXAMPLE_SENTRY_DSN`,
   pasting from your clipboard.

## Logging and metrics with Logfire

1. Goto https://pydantic.dev/logfire and sign-in - it's free for up to 10
   million spans/metrics per month.
2. Follow the instructions to create a new project and get the write token. Copy
   the value of the token into your clipboard.
3. For your local environment: Open your local `.env` file and set the
   `OE_PYTHON_TEMPLATE_EXAMPLE_LOGFIRE_TOKEN` variable to the value of the token from
   your clipboard. You can check `.env.example` for the correct format.
4. For the test, preview and production stage: Goto
   https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/settings/secrets/actions/new
   and create a new repository secret called `OE_PYTHON_TEMPLATE_EXAMPLE_SENTRY_DSN`,
   pasting from your clipboard.

## Uptime monitoring with betterstack

1. Goto https://betterstack.com/ and sign-in - it's free for up to 10 monitors
   and one status page
2. Create a monitor pointing to the `/api/v1/healthz` endpoint of your API on
   your production environment. As you enabled
   Vercel Serverless Function the URL should https://oe-python-template-example.vercel.app/api/v1/healthz
3. Create a status page in betterstack and add the monitor you created
4. Goto Advanced Settings / Github badge for your monitor on Betterstack and
   copy the badge for yaml
5. Run copier update and paste the snippet when asked for it

## Deploying webservice to Vercel as serverless function (optional)

1. Ensure you enabled Vercel deployment when creating or updating the project.
   If not, enable with `copier update`
2. Goto https://vercel.com/ and sign-in - it's free for solo devs and open
   source projects
3. Execute `pnpm i -g vercel@latest` to install or update the Vercel CLI, see
   https://vercel.com/docs/cli.
4. Execute `vercel login` to login to your Vercel account
5. In Vercel create a new project
6. Execute `vercel link` and link your repository to the newly created project
7. Execute `cat .vercel/project.json` to show the orgId and projectId
8. Goto
   https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/settings/secrets/actions/new
   and create a new repository secret called `VERCEL_ORG_ID`, copy and pasting
   from the output of step 6.
9. Goto
   https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/settings/secrets/actions/new
   and create a new repository secret called `VERCEL_PROJECT_ID`, copy and
   pasting from the output of step 6
10. Goto `https://vercel.com/account/tokens` and create a new token called
   `oe-python-template`. Copy the value of the token into your clipboard.
11. Goto
    https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/settings/secrets/actions/new
    and create a new repository secret called `VERCEL_TOKEN`, pasting from your
    clipboard.
12. In your Vercel project go to Settings > Deployment Protection, enable
    Protection Bypass for Automation, and copy the token it your clipboard.
13. Goto
    https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/settings/secrets/actions/new
    and create a new repository secret called `VERCEL_AUTOMATION_BYPASS_SECRET`, pasting from your
    clipboard. This is so the smoke test post deploy via GitHub Action can validate
    the deployment was successful.
14. Optional: In your Vercel project go to Settings > Environment Variables > Environments, and
      add environment variables with key 'OE_PYTHON_TEMPLATE_EXAMPLE_LOGFIRE_TOKEN' 
      and 'OE_PYTHON_TEMPLATE_EXAMPLE_SENTRY_DSN' - check your `.env` file for the values

## Polishing GitHub repository

1. Goto https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example
2. Click on the cogs icon in the top right corner next to about
4. Copy oe-python-template-example.readthedocs.io into the website field
3. Copy the description from the pyproject.toml file into the description field
5. Copy up to 20 tags from the pyproject.toml file into the topics field
6. Goto https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/settings and upload a soclial media image (e.g. logo.png) into the "Social preview" field
