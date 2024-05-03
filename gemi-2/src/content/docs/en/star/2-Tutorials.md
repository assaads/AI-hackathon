---
title: Starlight Project Tutorials 
description: Step-by-step guides to effectively utilize the features of the Starlight project. 
---

## Tutorial 1: Creating and Editing Content

This tutorial will guide you through the process of creating and editing content within your Starlight project.

### Step 1: Accessing Content Files

Navigate to the `src/content/` directory. Here, you will find Markdown or MDX files that contain the content for your website.

### Step 2: Modifying Existing Content

1.  Choose the Markdown or MDX file you want to edit.
2.  Open the file using your preferred text editor or IDE.
3.  Make the necessary changes to the content.
4.  Save the file. The development server will automatically update the site to reflect your edits.

### Step 3: Creating New Content

1.  Create a new Markdown or MDX file within the `src/content/` directory.
2.  Add frontmatter at the beginning of the file to define attributes such as the title and description:

```markdown
---
title: My New Page
description: This is a new page on my Starlight site.
---
```

3.  Write your content in Markdown or MDX format below the frontmatter.
4.  Save the file. Your new page will now be accessible on your Starlight site. 

## Tutorial 2: Customizing Site Metadata

This tutorial demonstrates how to personalize your Starlight site's metadata, including the title and description.

### Step 1: Open the Configuration File

Locate and open the `astro.config.mjs` file in the root directory of your project.

### Step 2: Edit Site Metadata

Within the `astro.config.mjs` file, find the `site` property. This property allows you to define various metadata attributes:

```javascript
export default defineConfig({
  // ... other configuration options
  site: 'https://example.com', // Replace with your domain
  markdown: {
    shikiConfig: {
      theme: 'dracula',
    },
  },
});
```

Modify the `title` and `description` fields to your desired values:

```javascript
export default defineConfig({
  // ... other configuration options
  site: 'https://example.com', // Replace with your domain
  markdown: {
    shikiConfig: {
      theme: 'dracula',
    },
  },
});
```

### Step 3: Save Changes

Save the `astro.config.mjs` file. The updated metadata will be reflected on your Starlight site.

## Tutorial 3: Adding a Sidebar

This tutorial will guide you through the process of incorporating a sidebar into your Starlight project to enhance navigation. 

### Step 1: Define Sidebar Configuration

Open the `astro.config.mjs` file and locate the `starlight` property within the configuration object.

### Step 2: Configure Sidebar Items

Within the `starlight` property, you will find the `sidebar` option. This option allows you to define an array of objects, where each object represents a section or page in your sidebar:

```javascript
// ... other configuration options
starlight({
  // ... other Starlight options
  sidebar: [
    {
      title: 'Section 1',
      items: [
        { title: 'Page 1', link: '/page-1' },
        { title: 'Page 2', link: '/page-2' },
      ],
    },
    {
      title: 'Section 2',
      items: [
        // ... page links for section 2
      ],
    },
  ],
}),
```

Customize the `title` and `link` properties of each item to match your content structure.

### Step 3: Save and Preview

Save the `astro.config.mjs` file. Your Starlight site will now display the configured sidebar, providing improved navigation for your users. 
