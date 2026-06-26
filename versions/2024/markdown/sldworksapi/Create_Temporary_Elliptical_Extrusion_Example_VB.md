---
title: "Create Temporary Elliptical Extrusion Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Temporary_Elliptical_Extrusion_Example_VB.htm"
---

# Create Temporary Elliptical Extrusion Example (VBA)

This example shows how to create a temporary elliptical body.

```vb
'------------------------------------------------
 ' Preconditions:
 ' 1. Open a model document.
 ' 2. Open an Immediate Window.
 '
 ' Postconditions:
 ' 1. Creates a temporary elliptical extruded body.
 ' 2. Examine the Immediate window.
 '------------------------------------------------
 Option Explicit
Sub main()
    Dim swApp           As SldWorks.SldWorks
     Dim swDocument      As SldWorks.ModelDoc2
     Dim swPart          As SldWorks.PartDoc
     Dim swModeler       As SldWorks.Modeler
    Dim swCurve(0)     As SldWorks.Curve
     Dim vCenter         As Variant
     Dim dMajorRadius    As Double
     Dim dMinorRadius    As Double
     Dim vMajorAxis      As Variant
     Dim vMinorAxis      As Variant
     Dim vEllipseParams  As Variant
     Dim aCenter(2)      As Double
     Dim aMajorAxis(2)   As Double
     Dim aMinorAxis(2)   As Double
     Dim dStartParam     As Double
     Dim dEndParam       As Double
     Dim bIsClosed       As Boolean
     Dim bIsPeriodic     As Boolean
     Dim bStatus         As Boolean

    Set swApp = Application.SldWorks
     Set swDocument = swApp.ActiveDoc

    If (swDocument Is Nothing) Then
         Set swDocument = swApp.NewPart
     End If

    If (swDocument.GetType <> swDocPART) Then
         Exit Sub
     End If

    Set swPart = swDocument
     Set swModeler = swApp.GetModeler

    aCenter(0) = 0#
     aCenter(1) = 0#
     aCenter(2) = 0#

    vCenter = aCenter

    dMajorRadius = 2#

    aMajorAxis(0) = 1#
     aMajorAxis(1) = 0#
     aMajorAxis(2) = 0#

    vMajorAxis = aMajorAxis

    dMinorRadius = 1#

    aMinorAxis(0) = 0#
     aMinorAxis(1) = 1#
     aMinorAxis(2) = 0#

    vMinorAxis = aMinorAxis
    Set swCurve(0) = swModeler.CreateEllipse(vCenter, dMajorRadius, dMinorRadius, vMajorAxis, vMinorAxis)

    If (swCurve(0) Is Nothing) Then
         Debug.Print " No curve"
     Else

        Debug.Print "Curve:"
         Debug.Print "  is ellipse  = " & IIf(swCurve(0).IsEllipse = False, "False", "True")
         Debug.Print "  type        = " & swCurve(0).Identity
         Debug.Print "  is ellipse  = " & (swCurve(0).Identity = swCurveTypes_e.ELLIPSE_TYPE)
         Debug.Print "  trimmed     = " & IIf(swCurve(0).IsTrimmedCurve = False, "False", "True")

        bStatus = swCurve(0).GetEndParams(dStartParam, dEndParam, bIsClosed, bIsPeriodic)

        Debug.Print "  start param = " & dStartParam
         Debug.Print "  end   param = " & dEndParam
         Debug.Print "  closed      = " & bIsClosed
         Debug.Print "  periodic    = " & bIsPeriodic

        Debug.Print "  length      = " & swCurve(0).GetLength3(dStartParam, dEndParam)

        If (Not (swCurve(0).IsEllipse = False)) Then
             vEllipseParams = swCurve(0).GetEllipseParams

            Debug.Print "  centre       = (" & vEllipseParams(0) & ", " & vEllipseParams(1) & ", " & vEllipseParams(2) & ")"
             Debug.Print "  major radius = " & vEllipseParams(3)
             Debug.Print "  major axis   = (" & vEllipseParams(4) & ", " & vEllipseParams(5) & ", " & vEllipseParams(6) & ")"
             Debug.Print "  minor radius = " & vEllipseParams(7)
             Debug.Print "  minor axis   = (" & vEllipseParams(8) & ", " & vEllipseParams(9) & ", " & vEllipseParams(10) & ")"
         End If

        Dim planeSurf As SldWorks.Surface
         Dim swMath As SldWorks.MathUtility
         Dim slotDepth As Double
         slotDepth = 0.01

        Set swMath = swApp.GetMathUtility
        Dim startArr(2) As Double
         Dim endArr(2) As Double
         Dim ptArr(2) As Double
         Dim dirArr(2) As Double
        ptArr(0) = 0#
         ptArr(1) = 0#
         ptArr(2) = 0#
         dirArr(0) = 0#
         dirArr(1) = 0#
         dirArr(2) = 1#
         startArr(0) = 1#
         startArr(1) = 0#
         startArr(2) = 0#
        Set planeSurf = swModeler.CreatePlanarSurface2((ptArr), (dirArr), (startArr))
        Dim profileBody As SldWorks.Body2
         Dim extrudedBody As SldWorks.Body2
         Dim dirVector As SldWorks.MathVector

        Set profileBody = planeSurf.CreateTrimmedSheet4((swCurve), True)
        dirArr(0) = 0#
         dirArr(1) = 0#
         dirArr(2) = -1#
        Set dirVector = swMath.CreateVector((dirArr))
         Set extrudedBody = swModeler.CreateExtrudedBody(profileBody, dirVector, slotDepth)
         extrudedBody.Display3 swDocument, RGB(1, 0, 0), 0
         swDocument.ViewZoomtofit

     End If

 End Sub
```
