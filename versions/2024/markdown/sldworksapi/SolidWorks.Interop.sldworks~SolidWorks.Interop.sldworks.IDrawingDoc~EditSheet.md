---
title: "EditSheet Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "EditSheet"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditSheet.html"
---

# EditSheet Method (IDrawingDoc)

Puts the current drawing sheet in edit mode.

## Syntax

### Visual Basic (Declaration)

```vb
Sub EditSheet()
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc

instance.EditSheet()
```

### C#

```csharp
void EditSheet()
```

### C++/CLI

```cpp
void EditSheet();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

## VBA Syntax

See

[DrawingDoc::EditSheet](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~EditSheet.html)

.

## Examples

[Place Note Behind Drawing Sheet (C#)](Place_Note_Behind_Drawing_Sheet_Example_CSharp.htm)

[Place Note Behind Drawing Sheet (VB.NET)](Place_Note_Behind_Drawing_Sheet_Example_VBNET.htm)

[Place Note Behind Drawing Sheet (VBA)](Place_Note_Behind_Drawing_Sheet_Example_VB.htm)

## Remarks

Subsequently created geometry resides on this drawing sheet.

You can use this method with[IDrawingDoc::EditSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~EditSketch.html)or[IDrawingDoc::EditTemplate](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~EditTemplate.html). Use[IDrawingDoc::GetEditSheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~GetEditSheet.html)to determine the current state.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)

[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
