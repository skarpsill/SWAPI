---
title: "GetActPlaneVector Method (IDimXpertAngleBetweenCircularDimTol)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertAngleBetweenCircularDimTol"
member: "GetActPlaneVector"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAngleBetweenCircularDimTol~GetActPlaneVector.html"
---

# GetActPlaneVector Method (IDimXpertAngleBetweenCircularDimTol)

## Syntax

### Visual Basic (Declaration)

```vb
Function GetActPlaneVector( _
   ByRef I As System.Double, _
   ByRef J As System.Double, _
   ByRef K As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertAngleBetweenCircularDimTol
Dim I As System.Double
Dim J As System.Double
Dim K As System.Double
Dim value As System.Boolean

value = instance.GetActPlaneVector(I, J, K)
```

### C#

```csharp
System.bool GetActPlaneVector(
   out System.double I,
   out System.double J,
   out System.double K
)
```

### C++/CLI

```cpp
System.bool GetActPlaneVector(
   [Out] System.double I,
   [Out] System.double J,
   [Out] System.double K
)
```

### Parameters

- `I`:
- `J`:
- `K`:

## See Also

[IDimXpertAngleBetweenCircularDimTol Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAngleBetweenCircularDimTol.html)

[IDimXpertAngleBetweenCircularDimTol Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAngleBetweenCircularDimTol_members.html)
