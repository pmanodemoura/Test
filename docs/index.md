## Welcome to GitHub Pages

You can use the [editor on GitHub](https://github.com/pmanodemoura/Test/edit/main/docs/index.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/pmanodemoura/Test/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.


<h1> Mapping Radius with Flexible Center Location </h1>

<a href="https://pmanodemoura.github.io/Test/respond-events"> Click here </a>

<script src= "https://public.tableau.com/javascripts/api/tableau-2.min.js" ></script>
<div id="tableauViz"></div>

function initializeViz() {
var placeholderDiv = document.getElementById("tableauViz");
var url = "http://public.tableau.com/views/MappingViewFlexible/MappingView";
var options = {
 width: '600px',
 height: '600px',
 hideTabs: true,
 hideToolbar: true,
 };
viz = new tableau.Viz(placeholderDiv, url, options);
}

