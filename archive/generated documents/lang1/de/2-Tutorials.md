---
title: Starlight-Tutorials
description: Entdecken Sie Schritt-für-Schritt-Anleitungen, um zu lernen, wie Sie verschiedene Starlight-Funktionen zum Erstellen Ihrer Dokumentationswebsite verwenden. 
---

## Inhalte erstellen und bearbeiten

### Neue Seiten hinzufügen 

1. **Markdown- oder MDX-Datei erstellen:** Erstellen Sie im Verzeichnis `src/content/docs` eine neue Datei mit der Erweiterung `.md` oder `.mdx`. Der Dateiname bestimmt den URL-Pfad für die Seite. Wenn Sie beispielsweise eine Datei mit dem Namen `getting-started.md` erstellen, wird eine Seite unter `/getting-started` zugänglich sein.

2. **Inhalt hinzufügen:** Schreiben Sie Ihren Dokumentationsinhalt mit Markdown-Syntax oder MDX, wenn Sie React-Komponenten einfügen müssen. 

3. **Frontmatter:** Fügen Sie am Anfang Ihrer Datei Frontmatter ein, um Metadaten wie Seitentitel und -beschreibung bereitzustellen. Hier ist ein Beispiel:

```md
---
title: Erste Schritte
description: Lernen Sie die Grundlagen der Verwendung von Starlight.
---

# Willkommen bei Starlight!

Dies ist Ihre Anleitung für die ersten Schritte...
``` 

### Vorhandene Seiten bearbeiten

1. **Datei suchen:** Suchen Sie im Verzeichnis `src/content/docs` die Markdown- oder MDX-Datei, die der Seite entspricht, die Sie bearbeiten möchten.

2. **Inhalt ändern:** Bearbeiten Sie den Inhalt mit Ihrem bevorzugten Texteditor. Sie können den Text ändern, neue Abschnitte hinzufügen oder das Frontmatter aktualisieren.

3. **Änderungen speichern:** Speichern Sie die Datei, und Ihre Änderungen werden auf der Dokumentationswebsite übernommen.


## Anpassen Ihrer Website

### Konfigurieren der Seitenleiste

1. **`astro.config.mjs` bearbeiten:** Öffnen Sie die Datei `astro.config.mjs` im Stammverzeichnis Ihres Projekts. 

2. **Option `sidebar` finden:** Suchen Sie die `starlight`-Integration und innerhalb ihrer Optionen finden Sie die Eigenschaft `sidebar`. Diese Eigenschaft ist ein Array von Objekten, die die Struktur und den Inhalt Ihrer Seitenleiste definieren. 

3. **Seitenleistenelemente ändern:** Sie können Seitenleistenelemente nach Bedarf hinzufügen, entfernen oder neu anordnen. Jedes Element sollte eine `text`-Eigenschaft für die angezeigte Beschriftung und eine `link`-Eigenschaft für den entsprechenden URL-Pfad haben. 

4. **Verschachtelung:** Um verschachtelte Abschnitte zu erstellen, verwenden Sie die Eigenschaft `items` innerhalb eines Seitenleistenelements. Diese Eigenschaft sollte ein Array von Objekten mit der gleichen Struktur wie Seitenleistenelemente der obersten Ebene sein.

5. **Änderungen speichern:** Speichern Sie die Datei `astro.config.mjs`, und die Seitenleiste wird auf der Dokumentationswebsite entsprechend aktualisiert. 


## Zusätzliche Tutorials

* **Verwenden von MDX:** Erfahren Sie, wie Sie React-Komponenten in Ihren Markdown-Inhalt integrieren.
* **Styling mit Tailwind CSS:** Entdecken Sie, wie Sie Tailwind CSS-Klassen verwenden, um das Erscheinungsbild Ihrer Dokumentationswebsite anzupassen.
* **Hinzufügen von Suchfunktionen:** Entdecken Sie, wie Sie Suchfunktionen implementieren, damit Benutzer relevante Informationen finden können.
* **Bereitstellen auf statischem Hosting:** Erhalten Sie Anweisungen zum Bereitstellen Ihrer Starlight-Website auf Plattformen wie Netlify oder Vercel. 
