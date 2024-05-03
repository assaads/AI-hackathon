import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

import tailwind from "@astrojs/tailwind";

// https://astro.build/config
export default defineConfig({
  integrations: [starlight({
    title: 'My Gemini Documentation',
    defaultLocale: 'en',
    locales: {
        // English docs in `src/content/docs/en/`
        'en': {
          label: 'English',
        },
        // Español docs in `src/content/docs/es/`
        'es': {
          label: 'Español',
          lang: 'es',
        },
    },
    social: {
      github: 'https://github.com/assaads/'
    }
  }), tailwind()]
});