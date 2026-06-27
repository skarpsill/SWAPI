---
title: "EMVEnableFeatures Enumeration"
project: "eDrawings API Help"
interface: "EMVEnableFeatures"
member: ""
kind: "enum"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.EMVEnableFeatures.html"
---

# EMVEnableFeatures Enumeration

Enable features. Bitmask.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum EMVEnableFeatures
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As EMVEnableFeatures
```

### C#

```csharp
public enum EMVEnableFeatures : System.Enum
```

### C++/CLI

```cpp
public enum class EMVEnableFeatures : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| eMVDisableGradientBackground | 65536 = Changes the eDrawings Viewer background from a gradient to solid color |
| eMVDisableMeasure | 32768 = Disables measure |
| eMVDisableMenuSave | 8 = Disable the Save selection on the File menu (Complete UI mode) |
| eMVDisableSNLCheckout | 8192 = Disable SNL checkout NOTE: If you disable SNL checkout, eDrawings Professional features may be disabled even if the document is review-enabled or if the eDrawings Professional license is present. |
| eMVEnableSilentMode | 16384 = Disable all dialogs |
| eMVEnableUICommands | 4194304 = When eDrawings is run as a COM object, user-interface (UI) commands are enabled |
| eMVFullUI | 16 = Display in Complete UI mode (preferred ) |
| eMVHLR | 256 = Display files saved in HLR (Hidden Lines Removed) display mode in HLR display mode |
| eMVReadOnly | 64 = Open the file as read only |
| eMVSeparateMarkup | 128 = Open all markup files associated with this file |
| eMVSimplifiedUI | 32 = Display in Simple UI mode |
| eMVSmallToolbarButtons | 2048 = Display Small toolbar buttons |
| eMVSuppressMarkupFileOpen | 4 = Do not display the File, Markup Open dialog |
| eMVSuppressMarkupOpenMenu | 512 = Disable the Open Markup selection on the File menu |
| eMVSuppressRMBMenu | 1024 = Disable the right-mouse button menu |
| eMVSuppressSavePrompt | 2 = Do not display the Save dialog even if the file was modified |
| eMVSupressMenuBar | 4096 = Hide the Menu toolbar |
| eMVTriad | 1 = Display triad |

## See Also

[eDrawings.Interop.EModelViewControl Namespace](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl_namespace.html)
