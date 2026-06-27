---
title: "Zoom to Region Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Zoom_to_Region_Example_VB.htm"
---

# Zoom to Region Example (VBA)

This example shows how to zoom to a specific region.

'------------------------------------------------------------------

' Problem:

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}This
sample code shows how to use:

'

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}IModelDoc2::ViewZoomTo2

'

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}The
input parameters may not be obvious, but

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}they
are related to the current view orientation.

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}The
code shows how to transform points

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}from
model space so that the resulting view is

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}zoomed
to points selected in model space.

'

' Preconditions:

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(1)
Part or assembly is open.

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(2)
Two points are picked in the graphics window.

'

' Postconditions:

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Graphics
area is zoomed to minimally include

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}the
two selection points.

'

'------------------------------------------------------------------

Option Explicit

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAppkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModViewkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelView

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swViewOrientkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.MathTransform

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swSelMgrkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SelectionMgr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swMathUtilkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.MathUtility

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vSelPt1kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vSelPt2kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swSelPt1kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.MathPoint

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swSelPt2kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.MathPoint

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
ikadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bRetkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = CreateObject("SldWorks.Application")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swMathUtil = swApp.GetMathUtility

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSelMgr = swModel.SelectionManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModView = swModel.ActiveView

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swViewOrient = swModView.Orientation3

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vSelPt1
= swSelMgr.GetSelectionPoint(1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vSelPt2
= swSelMgr.GetSelectionPoint(2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSelPt1 = swMathUtil.CreatePoint((vSelPt1))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSelPt2 = swMathUtil.CreatePoint((vSelPt2))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSelPt1 = swSelPt1.MultiplyTransform(swViewOrient)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSelPt2 = swSelPt2.MultiplyTransform(swViewOrient)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.ViewZoomTo2_

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelPt1.ArrayData(0), swSelPt1.ArrayData(1),
swSelPt1.ArrayData(2), _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSelPt2.ArrayData(0), swSelPt2.ArrayData(1),
swSelPt2.ArrayData(2)

End Sub

'-------------------------------------------
