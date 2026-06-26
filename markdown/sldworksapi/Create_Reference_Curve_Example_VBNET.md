---
title: "Create Reference Curve Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Reference_Curve_Example_VBNET.htm"
---

# Create Reference Curve Example (VB.NET)

```vb
This example shows how to create a reference curve by first creating a temporary spline curve.
```

```
'----------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part document template exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens a new part document.
' 2. Adds a reference curve to the part document.
' 3. Selects an endpoint on the reference curve
'    and prints to the Immediate window the
'    endpoint's position and coordinates.
' 4. Examine the graphics area and Immediate window.
'----------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swPart As PartDoc
        Dim swBody As Body2
        Dim swCurve(0) As Curve
        Dim vCurve As Object
        Dim swRefCurve As ReferenceCurve
        Dim swSelObj As Object
        Dim swSelMgr As SelectionMgr
        Dim swEdgePoint As EdgePoint
        Dim bRet As Boolean
        Dim nRetVal As Integer
        Dim iDim As Integer
        Dim iOrd As Integer
        Dim incp As Integer
        Dim iper As Integer
        Dim dprops(1) As Double
        Dim knots(9) As Double
        Dim cPoints(17) As Double
        Dim vprops As Object
        Dim vknots As Object
        Dim vcPoints As Object
        Dim selType As Integer
        Dim x As Double
        Dim y As Double
        Dim z As Double
        Dim iValueIn1 As Integer = 65535
        Dim iValueIn2 As Integer = 345
        Dim dValueOut As Double
        DoubleIntConv.Pack(iValueIn1, iValueIn2, dValueOut)
```

```
        'Open new part document and create a body
        swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2015\templates\Part.prtdot", 0, 0, 0)
        swPart = swModel
        swBody = swPart.CreateNewBody
```

```
        'Create a curve
        'Set properties
        iDim = 3 : iOrd = 4 : incp = 6 : iper = 0
        DoubleIntConv.Pack(iDim, iOrd, dprops(0))
        DoubleIntConv.Pack(incp, iper, dprops(1))
        vprops = dprops

        'Set knots
        knots(0) = 0 : knots(1) = 0 : knots(2) = 0 : knots(3) = 0
        knots(4) = 0.33096 : knots(5) = 0.72
        knots(6) = 1 : knots(7) = 1 : knots(8) = 1 : knots(9) = 1
        vknots = knots

        'Set control points
        cPoints(0) = 0 : cPoints(1) = 0 : cPoints(2) = 0
        cPoints(3) = 0.008703 : cPoints(4) = 0.016501 : cPoints(5) = 0
        cPoints(6) = 0.027636 : cPoints(7) = 0.052399 : cPoints(8) = 0
        cPoints(9) = 0.069472 : cPoints(10) = -0.011297 : cPoints(11) = 0
        cPoints(12) = 0.090421 : cPoints(13) = 0.017622 : cPoints(14) = 0
        cPoints(15) = 0.099188 : cPoints(16) = 0.029725 : cPoints(17) = 0
        vcPoints = cPoints

        'Create a spline curve
        swCurve(0) = swBody.AddProfileBspline((vprops), (vknots), (vcPoints))
        vCurve = swCurve

        'Create a reference curve
        swRefCurve = swModel.FeatureReferenceCurve(1, (vCurve), True, "", nRetVal)

        'Rebuild to display curve
        swModel.EditRebuild3()

        'Get endpoint on reference curve
        swModelDocExt = swModel.Extension
        bRet = swModelDocExt.SelectByID2("Unknown", "POINTREF", 0, 0, 0, False, 0, Nothing, 0)
        swSelMgr = swModel.SelectionManager
        selType = swSelMgr.GetSelectedObjectType3(1, -1)
        Debug.Print("Type of selection: " & selType)
        If swSelectType_e.swSelPOINTREFS = selType Then
            swSelObj = swSelMgr.GetSelectedObject6(1, -1)
            swEdgePoint = swSelObj
            Debug.Print(" Position of the endpoint: " & swEdgePoint.Position)
            swEdgePoint.GetPointCoordinates(x, y, z)
            Debug.Print(" Endpoint coordinates: " & x & ", " & y & ", and " & z)
        End If

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class

<System.Runtime.InteropServices.StructLayout(LayoutKind.Explicit)> Public Class DoubleIntConv

    'An 8-byte double contains 2 4-byte integers
    <System.Runtime.InteropServices.FieldOffset(0)> Private m_Int1 As Integer
    <System.Runtime.InteropServices.FieldOffset(4)> Private m_Int2 As Integer
    <System.Runtime.InteropServices.FieldOffset(0)> Private m_Double As Double

    Private Sub New(ByVal dValue As Double)
        'VB.NET wants these initialized in the constructor
        m_Int1 = 0
        m_Int2 = 0
        m_Double = dValue
    End Sub

    Private Sub New(ByVal iValue1 As Integer, ByVal iValue2 As Integer)
        'VB.NET wants these initialized in the constructor
        m_Double = 0.0
        m_Int1 = iValue1
        m_Int2 = iValue2
    End Sub

    ' Use an out parameter, so client code can pass in an uninitialized variable
    Public Shared Sub Pack(ByVal iIn1 As Integer, ByVal iIn2 As Integer, ByRef dOut As Double)
        Dim cv As DoubleIntConv
        cv = New DoubleIntConv(iIn1, iIn2)
        dOut = cv.m_Double
    End Sub

End Class
```
