---
title: Adding and Editing Content
description: Step-by-step guide for creating and modifying documentation pages in your Starlight site.
---

# Adding and Editing Content

Starlight uses Markdown and MDX files for creating documentation pages. This tutorial will guide you through adding new pages and editing existing content. 

## Adding a New Page

1. **Navigate to the `src/content/docs/` directory** in your project.
2. **Create a new Markdown file** with a descriptive name that reflects the content of the page. For example, if you're creating a guide on using a specific feature, you might name the file `using-feature-x.md`.
3. **Add frontmatter to the top of the file**. Frontmatter is metadata enclosed within `---` that provides information about the page, such as the title and description. Here's an example:

```markdown
---
title: Using Feature X
description: A guide to using the amazing features of Feature X.
---
```
4. **Write your content using Markdown syntax**. You can use headings, paragraphs, lists, links, images, and other Markdown elements to structure your documentation.
5. **(Optional) Use MDX for advanced features**. If you need to include interactive elements or embed components, you can use MDX. MDX allows you to write JSX within your Markdown files.
6. **Save the file**. Your new page will be automatically available on your documentation site at a route based on its filename. For example, the `using-feature-x.md` file will be accessible at `your-site.com/using-feature-x`.

## Editing an Existing Page

1. **Navigate to the `src/content/docs/` directory** and locate the Markdown or MDX file you want to edit.
2. **Open the file in your code editor** and make the necessary changes to the content or frontmatter.
3. **Save the file**. The changes will be reflected on your documentation site upon refresh.

## Tips for Writing Documentation

* **Keep it concise and clear**. Use simple language and avoid jargon.
* **Structure your content logically**. Use headings, subheadings, and lists to break up your content and make it easy to read.
* **Provide examples**. Illustrate your points with concrete examples to help users understand how things work.
* **Use visuals**. Include images, diagrams, and screenshots to enhance your documentation.
* **Test your documentation**. Make sure your instructions are accurate and easy to follow.


## Additional Resources

* **Starlight Documentation**: https://starlight.astro.build/
* **Markdown Guide**: https://www.markdownguide.org/
* **MDX Documentation**: https://mdxjs.com/


