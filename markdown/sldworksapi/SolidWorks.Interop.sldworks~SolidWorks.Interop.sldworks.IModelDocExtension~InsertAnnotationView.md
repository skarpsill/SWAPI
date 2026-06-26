---
title: "InsertAnnotationView Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "InsertAnnotationView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertAnnotationView.html"
---

# InsertAnnotationView Method (IModelDocExtension)

Inserts an annotation view in this part or assembly document.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertAnnotationView( _
   ByVal AnnotationViewingDirection As System.Integer, _
   ByVal DirectionReference As System.Object, _
   ByVal FlipDirection As System.Boolean, _
   ByVal HorizontalDirectionReference As System.Object, _
   ByVal AngleMadeWithHorizontal As System.Integer _
) As AnnotationView
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim AnnotationViewingDirection As System.Integer
Dim DirectionReference As System.Object
Dim FlipDirection As System.Boolean
Dim HorizontalDirectionReference As System.Object
Dim AngleMadeWithHorizontal As System.Integer
Dim value As AnnotationView

value = instance.InsertAnnotationView(AnnotationViewingDirection, DirectionReference, FlipDirection, HorizontalDirectionReference, AngleMadeWithHorizontal)
```

### C#

```csharp
AnnotationView InsertAnnotationView(
   System.int AnnotationViewingDirection,
   System.object DirectionReference,
   System.bool FlipDirection,
   System.object HorizontalDirectionReference,
   System.int AngleMadeWithHorizontal
)
```

### C++/CLI

```cpp
AnnotationView^ InsertAnnotationView(
   System.int AnnotationViewingDirection,
   System.Object^ DirectionReference,
   System.bool FlipDirection,
   System.Object^ HorizontalDirectionReference,
   System.int AngleMadeWithHorizontal
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `AnnotationViewingDirection`: Defined by either any

[swStandardViews_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swStandardViews_e.html)

enumerator or 0 for selection
- `DirectionReference`: If 0 specified for AnnotationViewingDirection, then specifiy a

[face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

or

[plane](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlane.html)

to define the direction of the annotation view
- `FlipDirection`: True to flip the annotation view in the opposite direction, false to notParamDesc
- `HorizontalDirectionReference`: An

[edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)

,

[sketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html)

, or

[face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)
- `AngleMadeWithHorizontal`: Angle used to make the annotation view horizontal

### Return Value

Newly inserted

[annotation view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotationView.html)

## VBA Syntax

See

[ModelDocExtension::InsertAnnotationView](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~InsertAnnotationView.html)

.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)

[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
