---
title: Erste Schritte mit Starlight
description: Erfahren Sie, wie Sie Starlight installieren, einrichten und mit der Erstellung Ihrer Dokumentationsseite beginnen.
---

## Einrichten Ihres Starlight-Projekts

### Voraussetzungen

Bevor Sie beginnen, stellen Sie sicher, dass Sie die folgenden Tools installiert haben:

* **Node.js:** Starlight basiert auf Node.js, daher müssen Sie es auf Ihrem System installiert haben. Laden Sie die neueste LTS-Version von der offiziellen Node.js-Website herunter und installieren Sie sie: https://nodejs.org/

### Installation 

1. **Neues Projekt erstellen:** Öffnen Sie Ihr Terminal und führen Sie den folgenden Befehl aus, um mit dem Astro CLI ein neues Starlight-Projekt zu erstellen:

```bash
npm create astro@latest -- --template starlight
```

2. **Abhängigkeiten installieren:** Navigieren Sie zu Ihrem neu erstellten Projektverzeichnis und installieren Sie die erforderlichen Abhängigkeiten:

```bash
npm install
```

## Starten des Entwicklungsservers

1. **Entwicklungsserver ausführen:** Verwenden Sie den folgenden Befehl, um den lokalen Entwicklungsserver zu starten: 

```bash
npm run dev 
```

2. **Zugriff auf Ihre Website:** Sobald der Server läuft, können Sie in Ihrem Webbrowser unter `http://localhost:4321` auf Ihre Starlight-Dokumentationswebsite zugreifen.

## Build für die Produktion

1. **Erstellen Sie Ihre Website:** Wenn Sie bereit sind, Ihre Dokumentationswebsite bereitzustellen, führen Sie den Build-Befehl aus:

```bash
npm run build
```

2. **Produktionsdateien:** Dieser Befehl generiert die produktionsbereiten Dateien im Verzeichnis `dist/` innerhalb Ihres Projekts. Sie können dieses Verzeichnis dann bei einem statischen Hosting-Dienst bereitstellen. 

