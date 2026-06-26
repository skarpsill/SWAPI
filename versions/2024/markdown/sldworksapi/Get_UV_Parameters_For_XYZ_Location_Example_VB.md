---
title: "Get UV Parameters for XYZ Location Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_UV_Parameters_For_XYZ_Location_Example_VB.htm"
---

# Get UV Parameters for XYZ Location Example (VBA)

This example shows how to use IFace2 and ICurve interfaces
to get the UV parameters from the XYZ location.

'-----------------------------------------------------------------------------
' Preconditions:
'kadov_tag{{<spaces>}}1. Openpublic_documents\samples\tutorial\cosmosxpress\aw_hook.sldprt.
'kadov_tag{{<spaces>}}2.
Verify that**Tools > System Options > Options ? FeatureManager > Solid Bodies**
' drop-down selection is**Show**.
'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}3.
Expand the Solid Bodies folder and select**Split Line1**.
' 4. Open the Immediate window or modify the macro to write the output to a
file.
'
' Postconditions: Observe
the output in the Immediate window.
'----------------------------------------------------------------------------

Option Explicit

Dim swApp As SldWorks.SldWorks

Dim swModel As SldWorks.ModelDoc2

Dim swSelMgr As SldWorks.SelectionMgr

Dim swFace As SldWorks.Face2

Dim vFaceSelPt As Variant

Sub main()

Set swApp = Application.SldWorks

Set swModel = swApp.**ActiveDoc**

Set swSelMgr = swModel.**SelectionManager**

Dim pntData(2) As Double

Dim swBody As Body2, procBody As Body2

Set swBody = swSelMgr.**GetSelectedObject6**(1, -1)

Dim skPnt As SketchPoint

Dim swFeat As Feature

'Set skPnt = swSelMgr.**GetSelectedObject6**(2, -1)

Set procBody = swBody.**GetProcessedBody2**(0.5, 0.5)

'Bypass surface split

Set swFace = procBody.**GetFirstFace**

'Set swFace = swBody.**GetFirstFace**

While Not swFace Is Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
uvBnds As Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}uvBnds
= swFace.GetUVBounds()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
UminFace As Double, UmaxFace As Double, VminFace As Double, VmaxFace As
Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}UminFace
= uvBnds(0): UmaxFace = uvBnds(1): VminFace = uvBnds(2): VmaxFace = uvBnds(3)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swSurf As Surface

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swSurf = swFace.**GetSurface**

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}uvBnds
= swSurf.**Parameterization**

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
UminSurf As Double, UmaxSurf As Double, VminSurf As Double, VmaxSurf As
Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}UminSurf
= uvBnds(0): UmaxSurf = uvBnds(1): VminSurf = uvBnds(2): VmaxSurf = uvBnds(3)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vEdges As Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vEdges
= swFace.**GetEdges**

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
i As Integer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
i = 0 To UBound(vEdges)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swEdge As Edge

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swEdge = vEdges(i)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swCurve As SldWorks.Curve

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swCurve = swEdge.**GetCurve**()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vCurveParams As Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vCurveParams
= swEdge.**GetCurveParams2**()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
startParam As Double, endParam As Double, incParam As Double, curParam
As Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}startParam
= vCurveParams(6)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}endParam
= vCurveParams(7)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}incParam
= (endParam - startParam) / 10#

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}curParam
= startParam

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}While
curParam < endParam

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vEdgePnt As Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vEdgePnt
= swEdge.**Evaluate**(curParam)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vSurfRevEval As Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vUVSurfParams As Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
UEdge As Double, VEdge As Double

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the UV parameters for the point using IFace2::ReverseEvaluate

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vUVSurfParams
= swFace.ReverseEvaluate(vEdgePnt(0),
vEdgePnt(1), vEdgePnt(2))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not IsEmpty(vUVSurfParams) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}UEdge
= vUVSurfParams(0): VEdge = vUVSurfParams(1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Edge point: " & vbCrLf & "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}x:
" & vEdgePnt(0) & vbCrLf & "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}y:
" & vEdgePnt(1) & vbCrLf & "kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}z:
" & vEdgePnt(2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"U parameter returned from IFace2::ReverseEvaluate is " &
UEdge

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
UEdge > UmaxFace Or UEdge < UminFace Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"U param error face"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'Stop

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"V parameter returned from IFace2::ReverseEvalute is " &
VEdge

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
VEdge > VmaxFace Or VEdge < VminFace Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"V param error face"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'Stop

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Else

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Face reverse evaluate fails - empty data"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get the UV parameters for the point using ICurve::ReverseEvaluate

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vUVSurfParams
= swSurf.ReverseEvaluate(vEdgePnt(0),
vEdgePnt(1), vEdgePnt(2))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not IsEmpty(vUVSurfParams) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}UEdge
= vUVSurfParams(0): VEdge = vUVSurfParams(1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"U parameter returned from ICurve::ReverseEvaluate is " &
UEdge

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
UEdge > UmaxFace Or UEdge < UminFace Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"U param error surface"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'Stop

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"V parameter returned from ICurve::ReverseEvaluate is " &
VEdge & vbCrLf

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
VEdge > VmaxFace Or VEdge < VminFace Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"V param error surface"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'Stop

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}curParam
= curParam + incParam

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Wend

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swFace = swFace.**GetNextFace**

Wend

Debug.Print "Complete"

End Sub
