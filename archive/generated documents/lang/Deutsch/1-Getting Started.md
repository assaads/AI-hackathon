---
title: Erste Schritte
description: Anleitung zur Installation, Einrichtung und Verwendung des Projekts für neue Benutzer.
---

# Einleitung
Willkommen zum Projekt! Dieser Leitfaden führt Sie durch die Installation, Einrichtung und grundlegende Verwendung.

## Voraussetzungen
Bevor Sie beginnen, stellen Sie sicher, dass Sie die folgenden Voraussetzungen erfüllen:

* **Node.js und npm:** Stellen Sie sicher, dass Sie die neueste Version von Node.js (https://nodejs.org) und npm (https://www.npmjs.com) installiert haben. 
* **Code-Editor:** Wählen Sie einen Code-Editor oder eine IDE Ihrer Wahl, z. B. Visual Studio Code (https://code.visualstudio.com).

## Installation
1. **Projekt klonen:** Klonen Sie das Projekt-Repository auf Ihren lokalen Computer. 
2. **Abhängigkeiten installieren:** Navigieren Sie im Terminal zum Projektverzeichnis und führen Sie den folgenden Befehl aus, um die erforderlichen Abhängigkeiten zu installieren:

```bash
npm install
```

## Einrichtung 
1. **Konfigurieren Sie die Umgebungsvariablen:** Erstellen Sie eine `.env`-Datei im Stammverzeichnis des Projekts und fügen Sie alle erforderlichen Umgebungsvariablen gemäß den Projektanforderungen hinzu.
2. **Starlight konfigurieren (optional):** Wenn Sie Starlight für die Dokumentation verwenden, passen Sie die Konfiguration in der Datei `astro.config.mjs` an.

## Anwendung starten
1. **Entwicklungsserver starten:** Führen Sie den folgenden Befehl aus, um den Entwicklungsserver zu starten:

```bash
npm run dev
```

Dadurch wird das Projekt gestartet und ist unter `http://localhost:3000` zugänglich.

2. **Projekt erstellen:** Um eine Produktionsversion des Projekts zu erstellen, verwenden Sie den folgenden Befehl:

```bash
npm run build
```

Dadurch wird das Projekt im Ordner `dist/` erstellt, der für die Bereitstellung bereit ist.

## Grundlegende Verwendung
Sobald das Projekt läuft, können Sie mit der Verwendung der Projektfunktionen beginnen. Weitere Informationen zur spezifischen Verwendung finden Sie in der Projektdokumentation. 
