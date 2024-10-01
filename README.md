# coconut-annotations

Annotations for the coconut dataset used in our thesis on on-tree clustered coconut detection and maturity classification.

## Setup

### 1. Install [Label Studio](https://labelstud.io/guide/install.html)

### 2. Clone this repository

```
git clone https://github.com/adriannebulao/coconut-annotations.git
```

### 3. Download dataset images into `storage/dataset/`

### 4. Set environment variables

- Allow Label Studio to access local file directories to import storage:

  On Windows:

  ```
  set LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED=true
  ```

  On Unix:

  ```
  export LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED=true
  ```

- Specify the root directory for Label Studio to use when accessing local file directories:

  On Windows:

  ```
  set LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT=.
  ```

  On Unix:

  ```
  export LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT=.
  ```

### 5. Run Label Studio

```
label-studio start -b -db "./label_studio.sqlite3"
```
