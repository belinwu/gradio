import gradio as gr

value = """
<script>
    alert("Hello, world!");
</script>
"""

with gr.Blocks() as demo:
    gr.HTML(value=value, as_iframe=False)

demo.launch()
