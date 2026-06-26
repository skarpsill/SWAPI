---
title: "swPDMDocManagerEvents_e Enumeration"
project: "SOLIDWORKS Toolbox Browser API"
interface: "swPDMDocManagerEvents_e"
member: ""
kind: "enum"
source: "toolboxapi/SolidWorks.Interop.swbrowser~SolidWorks.Interop.swbrowser.swPDMDocManagerEvents_e.html"
---

# swPDMDocManagerEvents_e Enumeration

Events to be handled by the PDM application.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swPDMDocManagerEvents_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swPDMDocManagerEvents_e
```

### C#

```csharp
public enum swPDMDocManagerEvents_e : System.Enum
```

### C++/CLI

```cpp
public enum class swPDMDocManagerEvents_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swAfterCopyingDocument | 9 = Notifies after Toolbox Browser copies or moves a PDM document |
| swAfterDeletingDocument | 7 = Notifies after Toolbox Browser deletes a PDM document |
| swAfterWritingToDocument | 3 = Notifies after Toolbox Browser writes to a PDM document |
| swBeforeCopyingDocument | 8 = Notifies before Toolbox Browser copies or moves a PDM document |
| swBeforeDeletingDocument | 6 = Notifies before Toolbox Browser deletes a PDM document |
| swBeforeWritingToDocument | 2 = Notifies before Toolbox Browser writes to a PDM document |
| swNewDocumentAdded | 5 = Notifies that Toolbox Browser has created a new PDM document or added a PDM document to the Toolbox Browser |
| swPDMDestroy | 1 = Notifies that the PDM application object is being destroyed |
| swPreInsertDocument | 4 = Notifies before Toolbox Browser inserts a PDM document into an assembly |

## See Also

[SolidWorks.Interop.swbrowser Namespace](SolidWorks.Interop.swbrowser~SolidWorks.Interop.swbrowser_namespace.html)
