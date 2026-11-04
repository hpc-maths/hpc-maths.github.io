# HPC@Maths website

Source of <https://hpc-maths.github.io/>, built with [Pelican](https://getpelican.com/) and deployed with GitHub Pages.

## Local build

```bash
pip install -r requirements.txt
pelican -s publishconf.py -t themes/hpc_math_theme/
python ics_generator.py
python -m http.server --directory public
```

The site is then available at <http://localhost:8000/>.

## Deployment

Every push to `master` runs `.github/workflows/pages.yml`, which builds the site and publishes it. Pull requests only run the build.
