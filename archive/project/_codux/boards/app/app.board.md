---
title: Create an 'Auth' Board with React Board and Wix
description: Learn how to set up an 'Auth' board using @wixc3/react-board for component visualization and rapid prototyping.
---

# Overview

This guide will walk you through the steps to create a new board, named 'Auth', using the `@wixc3/react-board` library. This board is designed to visualize the `App` component in an isolated environment, with specific configurations tailored for authentication workflows.

## Prerequisites

Before proceeding, make sure that you have the `@wixc3/react-board` library installed in your project. If not, you can install it with the following command:

```bash
npm install @wixc3/react-board --save-dev
```

Ensure that you also have the `App` component properly set up at `../../../App`.

## Step 1: Import Dependencies

Start by importing the `createBoard` function from `@wixc3/react-board`, as well as the `App` component, which you will visualize on the board.

```javascript
import { createBoard } from '@wixc3/react-board';
import App from '../../../App';
```

## Step 2: Create the Board

Utilize `createBoard` to define a new board with the following specifications:

- **Name**: Assign the board a name to identify it. In this case, it's 'Auth'.
- **Board**: Define a function that renders the `App` component.
- **isSnippet**: Indicate if the board should be treated as a code snippet. Here, we set it to `true` for simplicity.
- **environmentProps**: Add any environmental properties such as window background color.

Here's how you create the board:

```javascript
export default createBoard({
    name: 'Auth',
    Board: () => <App />,
    isSnippet: true,
    environmentProps: {
        windowBackgroundColor: '#f4f4f4',
    },
});
```

## Step 3: Using the Auth Board

After setting up the board, you can use it within your project to visualize the `App` component in an environment that mimics a typical authentication page. This allows you to quickly iterate and test UI components related to user authentication.

# Conclusion

You've successfully created a board named 'Auth' using the `@wixc3/react-board` library. This board environment is set up to help you develop and test components related to user authentication, with easily configurable environment properties.

Now you can integrate the board into your development workflow to streamline the component visualization and speed up the prototyping process.

For more advanced usage of `@wixc3/react-board` and component testing, check out the official documentation [here](https://github.com/wixplosives/react-board).
