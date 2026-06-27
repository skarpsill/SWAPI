---
title: "InsertSketchPictureData Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertSketchPictureData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSketchPictureData.html"
---

# InsertSketchPictureData Method (IModelDoc2)

Inserts a picture into the current sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertSketchPictureData( _
   ByVal Width As System.Short, _
   ByVal Height As System.Short, _
   ByVal PDataIn As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Width As System.Short
Dim Height As System.Short
Dim PDataIn As System.Integer

instance.InsertSketchPictureData(Width, Height, PDataIn)
```

### C#

```csharp
void InsertSketchPictureData(
   System.short Width,
   System.short Height,
   System.int PDataIn
)
```

### C++/CLI

```cpp
void InsertSketchPictureData(
   System.short Width,
   System.short Height,
   System.int PDataIn
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `Width`: Width of the image
- `Height`: Height of the image
- `PDataIn`: Pointer to a raw bitmap (HBITMAP) cast as a long

## VBA Syntax

See

[ModelDoc2::InsertSketchPictureData](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertSketchPictureData.html)

.

## Remarks

If your application must be x64 compatible, then use[IModelDoc2::InsertSketchPictureDatax64](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertSketchPictureDatax64.html).

A copy of the specified bitmap data is created. The SOLIDWORKS software does not release your bitmap object.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)

[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

[IModelDoc2::InsertSketchPicture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSketchPicture.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
