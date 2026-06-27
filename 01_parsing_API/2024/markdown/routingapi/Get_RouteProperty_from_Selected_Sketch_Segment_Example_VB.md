---
title: "Get Route Properties of Selected Sketch Segment Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Get_RouteProperty_from_Selected_Sketch_Segment_Example_VB.htm"
---

# Get Route Properties of Selected Sketch Segment Example (VBA)

This example shows how to get the route and covering properties of a sketch segment.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. In SOLIDWORKS, click Tools > Add-Ins > SOLIDWORKS Routing.
 ' 2. In Tools > Options > System Options > Routing > Routing File Locations,
 '    click Launch Routing Library Manager and set the locations of your
 '    SOLIDWORKS Routing files.
 ' 3. In the IDE, click Tools > References, select
 '    SOLIDWORKS version Routing Type Library, and click OK.
 ' 4. Open public_documents\samples\tutorial\api\RoutingAssem1.sldasm.
 ' 5. Add a covering to the longest cable.
 ' 6. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Edits Route1@Harness1^RoutingAssem1-1@RoutingAssem1.
 ' 2. Selects the Spline1 sketch segment.
 ' 3. Attempts to set the length of Spline1.
 ' 4. Prints the route and covering properties of Spline1.
 ' 5. Inspect the Immediate window.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 '----------------------------------------------------------------------------
 Option Explicit
     Dim swApp                As SldWorks.SldWorks
     Dim swModel              As SldWorks.ModelDoc2
     Dim swModelDoc           As SldWorks.ModelDocExtension
     Dim swTopLevelAssembly   As SldWorks.AssemblyDoc
     Dim rtRouteManager       As SWRoutingLib.RouteManager
     Dim rtCovering           As SWRoutingLib.Covering
     Dim bRetVal              As Boolean
     Dim rtRouteProperty      As SWRoutingLib.RouteProperty

Sub Main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swModelDoc = swModel.Extension
     Set swTopLevelAssembly = swModel
     Set rtRouteManager = swTopLevelAssembly.GetRouteManager
     If rtRouteManager Is Nothing Then
         Debug.Print "No RouteManager found in top-level document: " & swTopLevelAssembly.GetPathName
         Exit Sub
     End If

    ' Select the route
     bRetVal = swModelDoc.SelectByID2("Route1@Harness1^RoutingAssem1-1@RoutingAssem1", "ROUTEFABRICATED", 0, 0, 0, False, 0, Nothing, 0)
     swModel.EditRoute
    TestRoute swModelDoc, rtRouteManager

    rtRouteManager.ExitRoute
     swTopLevelAssembly.EditAssembly
End Sub

Private Sub TestRoute(swModelDoc As SldWorks.ModelDocExtension, rtRouteManager As SWRoutingLib.RouteManager)
    bRetVal = swModelDoc.SelectByID2("Spline1", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
    If (Not (bRetVal = False)) Then
        Set rtRouteProperty = rtRouteManager.GetRouteProperty
        If Not rtRouteProperty Is Nothing Then
            Dim dOriginalLength As Double
             dOriginalLength = rtRouteProperty.GetFixedLength
            Dim dNewLength As Double
             dNewLength = dOriginalLength * 1.1
            Dim lResult As Long
             lResult = rtRouteProperty.SetFixedLength(dNewLength)
            Dim dFinalLength As Double
             dFinalLength = rtRouteProperty.GetFixedLength

            Debug.Print "Spline1"
             Debug.Print "  Fixed length? " & (dOriginalLength < dFinalLength)
             If (dOriginalLength < dFinalLength) Then
                 Debug.Print "  Original fixed length (T0): " & dOriginalLength
                 Debug.Print "  Set fixed length result code as defined in swSetRouteFixedLengthError_e: " & lResult
                 Debug.Print "  Final fixed length (T1): " & dFinalLength
             End If

            Debug.Print "  Bend radius: " & rtRouteProperty.BendRadius
             Debug.Print "  Minimum bend radius: " & rtRouteProperty.MinimumBendRadius
             Debug.Print "  Route type as defined in swRouteType_e: " & rtRouteProperty.RouteType

            If (rtRouteProperty.HasCovering) Then
                 Set rtCovering = rtRouteProperty.GetCovering
                 Debug.Print "  Covering properties:"
                 Debug.Print "    Name: " & rtCovering.Name
                 Debug.Print "    Color: " & rtCovering.Color
                 Debug.Print "    Outer diameter: " & rtCovering.OuterDiameter
                 Debug.Print "    Part number: " & rtCovering.PartNumber
             End If

            Debug.Print ""
        End If
    End If
End Sub
```
