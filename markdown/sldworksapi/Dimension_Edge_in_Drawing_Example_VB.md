---
title: "Dimension Edge in Drawing Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Dimension_Edge_in_Drawing_Example_VB.htm"
---

# Dimension Edge in Drawing Example (VBA)

This examples shows how to dimension an edge in a drawing view.

'----------------------------------------------

'

' Problem:

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}This
example shows how to automatically add a

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}dimension
to a straight edge in all drawing views

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}in
which it appears. The edge geometry is transformed

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}to
the space of each drawing view and, depending on

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}whether
it is horizontal or vertical, an appropriate

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}style
of dimension is added.

'

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}This
example could form the basis for an application

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}to
automatically dimension a model when it is added to

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}a
drawing.

'

' Preconditions:

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(1)
Part or assembly is open.

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(2)
If an assembly, it is fully resolved.

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(3)
A straight edge is selected in the SOLIDWORKS graphics area.

'

' Postconditions:

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(1)
New drawing is created with three views.

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(2)
If possible, the previously selected edge

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}is
dimensioned in all drawing views.

'

' NOTE:kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}The
dimension is not created if

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}the
edge cannot be converted in a drawing view.

'

'----------------------------------------------

Option Explicit

Public Const LINE_TYPEkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Integer = 3001

Public Const CIRCLE_TYPEkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Integer = 3002

Public Const ELLIPSE_TYPEkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Integer = 3003

Public Const INTERSECTION_TYPEkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Integer = 3004

Public Const BCURVE_TYPEkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Integer = 3005

Public Const SPCURVE_TYPEkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Integer = 3006

Public Const CONSTPARAM_TYPEkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Integer = 3008

Public Const TRIMMED_TYPEkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Integer = 3009

' Define two types

Type DoubleRec

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}dValue
As Double

End Type

Type Long2Rec

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}iLower
As Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}iUpper
As Long

End Type

' Extract two integer values out of a single double value,

' by assigning a DoubleRec to the double value and

' copying the value over an Long2Rec and

' extracting the integer values.

Function ExtractFields _

( _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ByVal
dValue As Double, _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}iLower
As Long, _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}iUpper
As Long _

)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
drkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
DoubleRec

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
i2rkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long2Rec

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Set the double value

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}dr.dValue
= dValue

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Copy the values

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LSet
i2r = dr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Extract the values

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}iLower
= i2r.iLower

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}iUpper
= i2r.iUpper

End Function

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Const
sPathToTemplatekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
String = "c:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\data\templates\drawing.drtdot"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Const
nTolerancekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Double = 0.00000001

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Const
nXoffsetkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Double = 0.01

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Const
nYoffsetkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Double = 0.01

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAppkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swSelMgrkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SelectionMgr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swEdgekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Edge

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swEntkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.entity

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swCurvekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Curve

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vCurveParamkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
nDummykadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
nIdentitykadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
nTagkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
nSensekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swMathUtilkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.MathUtility

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
nPtData(2)kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vPtDatakadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelStartPtkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.MathPoint

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelEndPtkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.MathPoint

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swViewStartPtkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.MathPoint

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swViewEndPtkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.MathPoint

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swDrawkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.DrawingDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swDrawModelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swViewkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.view

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swViewXformkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.MathTransform

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vOutlinekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swDispDimkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.DisplayDimension

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
nXposkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
nYposkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bRetkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = CreateObject("SldWorks.Application")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSelMgr = swModel.SelectionManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swEdge = swSelMgr.GetSelectedObject5(1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swCurve = swEdge.GetCurve

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swEnt = swEdge

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vCurveParam
= swEdge.GetCurveParams2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ExtractFields
vCurveParam(8), nDummy, nIdentity

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ExtractFields
vCurveParam(9), nDummy, nTag

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ExtractFields
vCurveParam(10), nDummy, nSense

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Startkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
(" & vCurveParam(0) * 1000# & ", " & vCurveParam(1)
* 1000# & ", " & vCurveParam(2) * 1000# & ")
mm "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Endkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
(" & vCurveParam(3) * 1000# & ", " & vCurveParam(4)
* 1000# & ", " & vCurveParam(5) * 1000# & ")
mm "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Uparamkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
[" & vCurveParam(6) & ", " & vCurveParam(7)
& "]"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Identitykadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & nIdentity

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Tagkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & nTag

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Sensekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & nSense

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Derived quantity

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Lengthkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swCurve.GetLength2(vCurveParam(6),
vCurveParam(7)) * 1000# & " mm "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
""

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Only makes sense for straight edges

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
LINE_TYPE <> nIdentity Then Exit Sub

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swMathUtil = swApp.GetMathUtility

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nPtData(0)
= vCurveParam(0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nPtData(1)
= vCurveParam(1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nPtData(2)
= vCurveParam(2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vPtData
= nPtData

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModelStartPt = swMathUtil.CreatePoint(vPtData)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nPtData(0)
= vCurveParam(3)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nPtData(1)
= vCurveParam(4)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nPtData(2)
= vCurveParam(5)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vPtData
= nPtData

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModelEndPt = swMathUtil.CreatePoint(vPtData)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Start creating drawing of the model

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swDraw = swApp.NewDocument("C:\Program
Files\SOLIDWORKS\data\templates\drawing.drwdot", swDwgPaperAsize,
0, 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swDrawModel = swDraw

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bRet
= swDraw.Create3rdAngleViews2(swModel.GetPathName)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Assert
bRet

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swView = swDraw.GetFirstView

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swView = swView.GetNextView

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Do
While Not swView Is Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Select regardless

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bRet
= swView.SelectEntity(swEnt, False)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Assert
bRet

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vOutline
= swView.GetOutline

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swViewXform = swView.ModelToViewTransform

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swViewStartPt = swModelStartPt.MultiplyTransform(swViewXform)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swViewEndPt = swModelEndPt.MultiplyTransform(swViewXform)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Viewkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swView.Name

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Startkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
(" & swViewStartPt.ArrayData(0)
* 1000# & ", " & swViewStartPt.ArrayData(1)
* 1000# & ", " & swViewStartPt.ArrayData(2)
* 1000# & ") mm "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Endkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
(" & swViewEndPt.ArrayData(0)
* 1000# & ", " & swViewEndPt.ArrayData(1)
* 1000# & ", " & swViewEndPt.ArrayData(2)
* 1000# & ") mm "

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
""

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Abs(swViewStartPt.ArrayData(0)
- swViewEndPt.ArrayData(0)) <
nTolerance Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Must be vertical

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Place dimension midway up edge and to the right of view

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nXpos
= vOutline(0) - nXoffset

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nYpos
= Abs((swViewStartPt.ArrayData(1)
+ swViewEndPt.ArrayData(1)) /
2#)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
NULL if cannot convert edge in this view

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swDispDim = swDrawModel.AddVerticalDimension2(nXpos,
nYpos, 0#)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
Abs(swViewStartPt.ArrayData(1)
- swViewEndPt.ArrayData(1)) <
nTolerance Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Must be horizontal

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Place dimension midway across edge and above view

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nXpos
= Abs((swViewStartPt.ArrayData(0)
+ swViewEndPt.ArrayData(0)) /
2#)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nYpos
= vOutline(3) + nYoffset

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
NULL if cannot convert edge in this view

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swDispDim = swDrawModel.AddHorizontalDimension2(nXpos,
nYpos, 0#)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Else

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Neither horizontal or vertical

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Place dimension near middle of edge

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nXpos
= Abs((swViewStartPt.ArrayData(0)
+ swViewEndPt.ArrayData(0)) /
2#) + nXoffset

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}nYpos
= Abs((swViewStartPt.ArrayData(1)
+ swViewEndPt.ArrayData(1)) /
2#) + nYoffset

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Depends on the orientation of the entity in the drawing view,

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
thus, could be NULL

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Create the dimension even if the entity is not

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
visible in the drawing view

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swDispDim = swDrawModel.AddDimension2(nXpos,
nYpos, 0#)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swView = swView.GetNextView

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Loop

End Sub

'-------------------------------------------
