---
title: "AddPage Method (ISWPropertySheet)"
project: "SOLIDWORKS API Help"
interface: "ISWPropertySheet"
member: "AddPage"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet~AddPage.html"
---

# AddPage Method (ISWPropertySheet)

Adds a CPropertyPage-derived page to an

[ISWPropertySheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISWPropertySheet.html)

.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddPage( _
   ByVal Page As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISWPropertySheet
Dim Page As System.Integer
Dim value As System.Integer

value = instance.AddPage(Page)
```

### C#

```csharp
System.int AddPage(
   System.int Page
)
```

### C++/CLI

```cpp
System.int AddPage(
   System.int Page
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `Page`: Pointer to the CPropertyPage to add, cast to a long

### Return Value

True if successful, false if not

## VBA Syntax

See

[SWPropertySheet::AddPage](ms-its:sldworksapivb6.chm::/sldworks~SWPropertySheet~AddPage.html)

.

## Remarks

If your application must be x64 compatible, then use

[ISWPropertySheet::AddPagex64](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISWPropertySheet~AddPagex64.html)

.

## See Also

[ISWPropertySheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet.html)

[ISWPropertySheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet_members.html)
