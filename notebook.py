# Copyright 2024 Marimo. All rights reserved.

import marimo

__generated_with = "0.11.31"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        This is a demo of the features of Marimo!
        """
    ).callout()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        # What is Marimo

        Marimo is a Notebook environment with advanced features that are simply not present in **Jupyter Notebook**

        # Features


        ## Reactivity

        Writing Jupyter notebooks, one of the frustrating part is you have to run the cells from start to finish if any variables or functions are changed.

        Jupyter does allow Reactivity as part of extensions like [ipyflow](https://github.com/ipyflow/ipyflow), but in Marimo it is battery included.
        Marimo knows all the values in the cell and creates a dependency graph between them. So whenever a glboal variable is changed, it **automagically** updates all the cells that has that variable.


        ## Plain python

        Unlike Jupyter notebook that has `ipynb` which is niether git-friendly or clean code friendly; Marimo provides a notebook-like experience in pure python. All marimo related code is part of decorators.

        ## Components

        It has components support such as Button, Graph, Slider, Code Snippet and much more!


        ## WASM Support

        It allows to be exported as WASM module. This is deployed in Cloudflare pages but can also be exported to Github pages.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    # UI
    slider = mo.ui.slider(start=1, stop=20, label="Slider", value=3)
    date = mo.ui.date("2022-02-01")
    button = mo.ui.button(
        value=0,
        label="increment",
        on_click=lambda value: value+1)
    initial_code = """
    const a: number;
    console.log("Hello world")
    """

    editor = mo.ui.code_editor(
        value=initial_code,
        language="typescript"
    )
    # cars = pd.DataFrame(json.loads(
    #   pyodide.http.open_url('https://vega.github.io/vega-datasets/data/cars.json').read()
    # ))
    # chart = mo.ui.altair_chart(alt.Chart(cars).mark_point().encode(
    #     x='Horsepower',
    #     y='Miles_per_Gallon',
    #     color='Origin'
    # ))
    return button, date, editor, initial_code, slider


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ## 4. Running notebooks as apps

        marimo notebooks can double as apps. Click the app window icon in the
        bottom-right to see this notebook in "app view."

        Serve a notebook as an app with `marimo run` at the command-line.
        Of course, you can use marimo just to level-up your
        notebooking, without ever making apps.
        """
    )
    return


@app.cell
def _(mo):
    mo.md("""# PDF Example""")
    return


@app.cell
def _(mo):
    # PDF

    mo.pdf(
        src="https://arxiv.org/pdf/2104.00282.pdf",
        width="100%",
        height="100vh",
    )
    # mo.video("https://v3.cdnpk.net/videvo_files/video/free/2013-08/large_watermarked/hd0992_preview.mp4")
    return


@app.cell
def _(mo):
    mo.video("https://v3.cdnpk.net/videvo_files/video/free/2013-08/large_watermarked/hd0992_preview.mp4")
    return


if __name__ == "__main__":
    app.run()
