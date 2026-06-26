---
title: "Get Tolerance Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Tolerance_Example_VB.htm"
---

# Get Tolerance Example (VBA)

This example shows how to get the tolerance of a model.

'---------------------------------------------

Option Explicit

Public Enum swTolerances_e

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swBSCurveOutputTol
= 0

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swBSCurveNonRationalOutputTol
= 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swUVCurveOutputTol
= 2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSurfChordTessellationTol
= 3

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swSurfAngularTessellationTol
= 4

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swCurveChordTessellationTol
= 5

End Enum

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAppkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelerkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Modeler

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModeler = swApp.GetModeler

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Modeler Tolerances:"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}BSCurveOutputTolkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swModeler.GetToleranceValue(swBSCurveOutputTol)
* 1000# & " mm"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}BSCurveNonRationalOutputTolkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}= "
& swModeler.GetToleranceValue(swBSCurveNonRationalOutputTol)
* 1000# & " mm"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}UVCurveOutputTolkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swModeler.GetToleranceValue(swUVCurveOutputTol)
* 1000# & " mm"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SurfChordTessellationTolkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swModeler.GetToleranceValue(swSurfChordTessellationTol)
* 1000# & " mm"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SurfAngularTessellationTolkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swModeler.GetToleranceValue(swSurfAngularTessellationTol)
* 1000# & " mm"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CurveChordTessellationTolkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swModeler.GetToleranceValue(swCurveChordTessellationTol)
* 1000# & " mm"

End Sub

'---------------------------------------------
