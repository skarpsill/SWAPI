---
title: "SetTitleBitmap Method (IPropertyManagerPage2)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPage2"
member: "SetTitleBitmap"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~SetTitleBitmap.html"
---

# SetTitleBitmap Method (IPropertyManagerPage2)

Obsolete. Superseded by

[IPropertyManagerPage2::SetTitleBitmap2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~SetTitleBitmap2.html)

.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetTitleBitmap( _
   ByVal ModuleHandle As System.Integer, _
   ByVal Identifier As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2
Dim ModuleHandle As System.Integer
Dim Identifier As System.Integer
Dim value As System.Boolean

value = instance.SetTitleBitmap(ModuleHandle, Identifier)
```

### C#

```csharp
System.bool SetTitleBitmap(
   System.int ModuleHandle,
   System.int Identifier
)
```

### C++/CLI

```cpp
System.bool SetTitleBitmap(
   System.int ModuleHandle,
   System.int Identifier
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `ModuleHandle`:
- `Identifier`:

## VBA Syntax

See

[PropertyManagerPage2::SetTitleBitmap](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPage2~SetTitleBitmap.html)

.

## See Also

[IPropertyManagerPage2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.html)

[IPropertyManagerPage2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2_members.html)
