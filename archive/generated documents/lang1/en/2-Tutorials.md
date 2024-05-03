---
title: Starlight Tutorials 
description: Explore step-by-step guides to learn how to use various Starlight features for building your documentation site.
---

## Creating and Editing Content

### Adding New Pages

1. **Create a Markdown or MDX file:** Inside the `src/content/docs` directory, create a new file with the `.md` or `.mdx` extension. The file name will determine the URL path for the page. For example, creating a file named `getting-started.md` will result in a page accessible at `/getting-started`.

2. **Add content:** Write your documentation content using Markdown syntax or MDX if you need to include React components.

3. **Frontmatter:** Include frontmatter at the beginning of your file to provide metadata such as the page title and description. Here's an example:

```md
---
title: Getting Started
description: Learn the basics of using Starlight.
---

# Welcome to Starlight!

This is your getting started guide...
```

### Editing Existing Pages

1. **Locate the file:** Find the Markdown or MDX file corresponding to the page you want to edit within the `src/content/docs` directory.

2. **Modify content:** Edit the content using your preferred text editor. You can change the text, add new sections, or update the frontmatter. 

3. **Save changes:** Save the file, and your changes will be reflected on the documentation site.


## Customizing Your Site

### Configuring the Sidebar

1. **Edit `astro.config.mjs`:** Open the `astro.config.mjs` file in the root of your project.

2. **Find the `sidebar` option:** Locate the `starlight` integration and within its options, you'll find the `sidebar` property. This property is an array of objects that define the structure and content of your sidebar.

3. **Modify sidebar items:** You can add, remove, or reorder sidebar items as needed. Each item should have a `text` property for the displayed label and a `link` property for the corresponding URL path.

4. **Nesting:** To create nested sections, use the `items` property within a sidebar item. This property should be an array of objects with the same structure as top-level sidebar items. 

5. **Save changes:** Save the `astro.config.mjs` file, and the sidebar will update accordingly on the documentation site.


## Additional Tutorials

* **Using MDX:** Learn how to integrate React components into your Markdown content.
* **Styling with Tailwind CSS:** Explore how to use Tailwind CSS classes to customize the appearance of your documentation site. 
* **Adding Search Functionality:** Discover how to implement search functionality to help users find relevant information.
* **Deploying to Static Hosting:** Get instructions on deploying your Starlight site to platforms like Netlify or Vercel. 
