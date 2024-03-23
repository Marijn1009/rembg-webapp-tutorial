Full credit for code to [codediodeio](https://github.com/codediodeio/rembg-webapp-tutorial).

Goal this repo: Have some fun with python & docker. Learn how to make the premade flask app accessible to localhost and access it from there.

# Text from original Fireship repo

A simple flask app to remove the background of an image with [Rembg](https://github.com/danielgatis/rembg)

Watch the [tutorial](https://youtu.be/cw34KMPSt4k) on YouTube

### Run it

```
pip install -r requirements.txt
python app.py
```

# My own notes

### Troublesooting python install
Download python from official web page. Test in terminal ```python --version``` to see if it is working.

Problems:
- Microsoft store alias: Remove aliases to microsoft store via search 'Apps & Features' > 'App execution aliases'. Turn it off for Python. Then when using command line 'python' it will use the manually installed instance.
- PATH: Turn on option to extend path length when installing python. Then restart pc and it works. 

Restart VS code and right bottom it should no longer say 'missing interpreter' and recognize the installed python. 

Install dependencies: Use ```pip install xxx``` or in bulk use ```pip install -r reequirements.txt```.

### Ways to remove background
- Run fully within python manually: Add image to directory. Run basic.py to remove background from 1 image and save it into the directory.
- Deploy app from local python: Run the app.py script. (Either ```python app.py``` in terminal, or from VS code press run. It's the same.)
- Use docker container:
    - Make sure 'Docker desktop' is started so Docker deamon is running
    - Build image and give it a name: ```docker build -t image_rmbg .``` (see created images using ```docker images```)
    - Run image, give it a name and expose a port: ```docker run --name my_rmbg -p 5100:5100 image_rmbg```
        - The app is hard-coded in app.py to use port 5100, so it needs to be x:5100. But the first one can be any port on the host machine that you want to map. For example 8000:5100 and access it via localhost:8000.
    - Access the app at website `localhost:5100'

### Publish to github
Setup:
```console
git remote set-url origin https://github.com/Marijn1009/rembg-webapp-tutorial.git
git push -u origin main
```

Then add, commit and push new changes:
```console
git commit -a -m "Message"
git push
```

