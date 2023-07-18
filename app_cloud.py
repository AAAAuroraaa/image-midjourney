#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template, request
import openai,os

app = Flask(__name__)

os.environ["REPLICATE_API_TOKEN"] = "r8_JriM9gnBo57NPGV4NCSyof36DccFYBl1hjHLN"
model = replicate.models.get("tstramer/midjourney-diffusion")
version = model.versions.get("436b051ebd8f68d23e83d22de5e198e0995357afef113768c20f0b6fcef23c8b")

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        t = request.form.get("txt")
        inputs = {'prompt': t}
        output = version.predict(**inputs)
        return(render_template("image_app.htm", result=output))
    else:
        return(render_template("image_app.htm",result="waiting"))

if __name__ == "__main__" :
    app.run()

