app = Flask(__name__)
run_with_ngrok(app)

@app.route('/image/create')
def create():
  query = request.args.get('query')
  outputs=[]
  prompts = [
      ImaginePrompt(query),
  ]
  for result in imagine(prompts):
    display(result.img)
    outputs.append(result.img)

@app.route('/image/edit')
def edit():
  query = request.args.get('query')
  p = ImaginePrompt(
      query,
      prompt_strength=7.5,
      init_image=LazyLoadingImage(url="https://raw.githubusercontent.com/brycedrennan/imaginAIry/7100d3f9eae5834c7ca512304b7475825a7f40f1/assets/girl_with_a_pearl_earring.jpg"),
      init_image_strength=0.1,
      control_inputs=[ControlInput(mode="edit")]
  )
  prompts = [p]
  for result in imagine(prompts):
      display(result.img)



if __name__ == '__main__':
  app.run()
