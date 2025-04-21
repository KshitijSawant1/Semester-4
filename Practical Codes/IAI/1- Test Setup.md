Here’s a **complete setup guide** for installing and configuring **Java**, **Python**, and **virtual environments** in **Visual Studio Code (VS Code)**:

---

### ✅ **Step 1: Install VS Code**

1. Go to: [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. Download and install VS Code for your platform (Windows/macOS/Linux).

---

### ✅ **Step 2: Install Java**

#### For Windows:

- Download the **JDK** from [https://adoptium.net/](https://adoptium.net/) (Recommended: Temurin JDK 17).
- Install and note the installation path.
- Add to Environment Variables:
  - `JAVA_HOME` → set to JDK path (e.g., `C:\Program Files\Eclipse Adoptium\jdk-17`)
  - Add `JAVA_HOME\bin` to your `Path`.

#### For macOS:

```bash
brew install openjdk@17
sudo ln -sfn /opt/homebrew/opt/openjdk@17/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk
```

#### Test Java:

```bash
java -version
javac -version
```

---

### ✅ **Step 3: Install Python**

#### Windows/macOS:

- Download from [https://www.python.org/downloads/](https://www.python.org/downloads/)
- Ensure you check ✅ **"Add Python to PATH"** during installation.

#### Test Python:

```bash
python --version
pip --version
```

---

### ✅ **Step 4: Install VS Code Extensions**

In VS Code, open the Extensions panel (Ctrl+Shift+X or Cmd+Shift+X), and install:

- **Python** by Microsoft
- **Java Extension Pack** by Microsoft
- **Code Runner** (optional for fast code execution)
- **Jupyter** (for .ipynb notebooks)
- **Pylance** (for enhanced Python experience)

---

### ✅ **Step 5: Set Up Python Virtual Environment (venv)**

1. Open a folder in VS Code (File → Open Folder).
2. Open a terminal (Ctrl+` or View → Terminal).
3. Create venv:

```bash
python -m venv .venv
```

4. Activate:

   - **Windows**:
     ```bash
     .venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source .venv/bin/activate
     ```

5. VS Code will detect `.venv` and show a popup to select interpreter → Click “Yes”.

---

### ✅ **Step 6: Configure Java in VS Code**

1. In VS Code, open `Command Palette (Ctrl+Shift+P)` → “Java: Configure Java Runtime”.
2. Select installed JDK.
3. You can compile `.java` files with:

```bash
javac FileName.java
java FileName
```

4. Or click the **Run** ▶️ icon in the top right.

---

### ✅ **Step 7: Run & Debug**

- For Python: Select interpreter → press `F5` or right-click file → “Run Python File”.
- For Java: Right-click → “Run Java”, or use main method and run from the top-right button.

---

### ✅ Optional Tools:

- **Git**: [https://git-scm.com/](https://git-scm.com/) for version control.
- **Node.js**: [https://nodejs.org/](https://nodejs.org/) if you plan to use web dev tools.

---

If you want, I can provide:

- ✅ Launch.json and settings.json for Java/Python projects
- ✅ VS Code theme or productivity plugin recommendations
- ✅ Setup walkthrough for Django, Flask, Spring, Maven, or any framework

Let me know what you want next.
