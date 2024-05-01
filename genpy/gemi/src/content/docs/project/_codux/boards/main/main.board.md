---
title: Creating a Main Component Board with Wix React Board
description: A guide on how to use the '@wixc3/react-board' package to create a board for the 'Main' component.
---

# Introduction
This guide walks you through the process of creating a board for the `Main` component using `@wixc3/react-board`. Boards are a part of the Wix React development environment and allow you to define a structured context for previewing, testing, and showcasing components.

## Prerequisites
- Ensure you have the `@wixc3/react-board` package installed in your project.
- Familiarity with React components and JSX syntax is recommended.

# Step 1: Importing Dependencies
Begin by importing the `createBoard` function from the `@wixc3/react-board` package. Additionally, import the `Main` component from your components directory, typically found within your project's `components/main` folder.

```javascript
import { createBoard } from '@wixc3/react-board';
import { Main } from '../../../components/main/main';
```

## Understanding Imports
- `createBoard`: A higher-order function provided by `@wixc3/react-board` for creating board configurations.
- `Main`: Your custom React component that you want to create a board for.

# Step 2: Creating the Board Configuration
Use the `createBoard` function to define the configuration for your `Main` component board. The configuration object should include:
- `name`: A string that serves as the name of your board.
- `Board`: A functional component returning the JSX for the `Main` component.
- `isSnippet`: A Boolean indicating whether the board is a snippet, which is typically used for smaller preview components within documentation.

```javascript
export default createBoard({
    name: 'Main',
    Board: () => <Main />,
    isSnippet: true,
});
```

## Understanding the Configuration Object
- `name` is how you will reference this particular board within your project or documentation.
- `Board` is a function returning the JSX of your `Main` component.
- `isSnippet` when set to true, signifies that this board's purpose is primarily for quick examples or snippets in documentation.

# Step 3: Usage and Integration
After creating the board configuration, your new board for the `Main` component can now be used within your project's documentation or development tools that support Wix React Boards.

- Integrate the board in your documentation site.
- Use the board for showcasing the component within a development environment.

# Conclusion
You've learned how to create a board configuration for the `Main` component using `@wixc3/react-board`. This guide explained the purpose of boards, walked you through the creation and configuration of a board, and described how to integrate it into your workflow.

For more information on working with boards, please refer to the official [`@wixc3/react-board` documentation](https://github.com/wixplosives/react-board).

- Experiment with the created board by adding properties and context to the `Main` component as needed.
- Use boards to improve the component development process by providing isolated, easily shareable examples of components in use.