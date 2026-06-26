---
title: "swInterfaceBrightnessColor_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swInterfaceBrightnessColor_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swInterfaceBrightnessColor_e.html"
---

# swInterfaceBrightnessColor_e Enumeration

Background colors.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swInterfaceBrightnessColor_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swInterfaceBrightnessColor_e
```

### C#

```csharp
public enum swInterfaceBrightnessColor_e : System.Enum
```

### C++/CLI

```cpp
public enum class swInterfaceBrightnessColor_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swIBColor_ActiveTabColor | 3 = Color of a tab's fill area when the tab is active |
| swIBColor_ButtonFillCheckedAndHotColor | 8 = Color of the CommandManager flat-style button's fill area |
| swIBColor_ButtonFillCheckedColor | 6 = Color of the CommandManager flat-style button's fill area |
| swIBColor_ButtonFillHotColor | 5 = Color of the CommandManager flat-style button's fill area |
| swIBColor_ButtonFillPressedColor | 7 = Color of the CommandManager flat-style button's fill area when pressing and holding down the left button of the mouse |
| swIBColor_DisabledTextColor | 2 = Color of text when text is disabled |
| swIBColor_EnabledTextColor | 1 = Color of text when text is enabled |
| swIBColor_FeatureMgrBkgnd | 0 = Background color is the same as the FeatureManager design tree's background color |
| swIBColor_InactiveTabColor | 4 = Color of a tab's fill area when the tab is inactive |

## Remarks

If you want your add-in to use the same colors for your buttons as used by the SOLIDWORKS CommandManager buttons, then you can query and use these values.

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
