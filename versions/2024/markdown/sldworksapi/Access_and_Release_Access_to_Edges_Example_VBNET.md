---
title: "Access Edges on Rip Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Access_and_Release_Access_to_Edges_Example_VBNET.htm"
---

# Access Edges on Rip Feature Example (VB.NET)

This example shows how to access edges on a rip feature.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Verify that the specified model document exists.
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Opens the specified part.
 ' 2. Creates Shell1 and Rip1 features.
  ' 3. Inspect the FeatureManager design tree, the graphics area, and
 '    the Immediate window.
 '
  ' NOTE: Because the model is used elsewhere, do not save changes.
  '----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()

         Dim swModel As ModelDoc2
         Dim swSelMgr As SelectionMgr
         Dim swFeat As Feature
         Dim swRip As RipFeatureData
         Dim vEdge As Object
         Dim swEdge As Edge
         Dim swEnt As Entity
         Dim i As Integer
         Dim lRipDirection As Integer
         Dim bRet As Boolean
         Dim longstatus As Integer, longwarnings As Integer

         lRipDirection = 64

         swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\box.sldprt", 1, 0, "", longstatus, longwarnings)
         swApp.ActivateDoc2("box", False, longstatus)
         swModel = swApp.ActiveDoc
         swSelMgr = swModel.SelectionManager

         bRet = swModel.Extension.SelectByID2("", "FACE", -0.0566885410894997, 0.0299999999999159, 0.0200993374069753, False, 1, Nothing, 0)
         swModel.InsertFeatureShell(0.01, False)

         bRet = swModel.Extension.SelectByID2("", "EDGE", 0.0441585455038194, 0.0151990980971277, 0.0459121462268968, True, lRipDirection, Nothing, 0)
         swModel.InsertRip(0.0001)

         bRet = swModel.Extension.SelectByID2("Rip1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
         swFeat = swSelMgr.GetSelectedObject6(1, -1)

         ' Get rip feature data
         swRip = swFeat.GetDefinition

         Debug.Print("Gap: " & swRip.Gap * 1000.0# & " mm")

         bRet = swRip.AccessSelections(swModel, Nothing)

         Debug.Print("Number of edges: " & swRip.GetEdgesCount)

         swModel.ClearSelection2(True)

         vEdge = swRip.Edges

         For i = 0 To UBound(vEdge)
             swEdge = vEdge(i)
             swEnt = swEdge

             Debug.Print("Direction of rip for edge (0=current, 1=other, 2=both): " & swRip.GetDirection(swEdge))

             bRet = swEnt.Select4(True, Nothing)
         Next i

         swRip.ReleaseSelectionAccess()

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
