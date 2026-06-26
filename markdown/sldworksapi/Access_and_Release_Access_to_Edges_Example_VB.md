---
title: "Access Edges on Rip Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Access_and_Release_Access_to_Edges_Example_VB.htm"
---

# Access Edges on Rip Feature Example (VBA)

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
Option Explicit
Sub main()
    Dim swApp                   As SldWorks.SldWorks
     Dim swModel                 As SldWorks.ModelDoc2
     Dim swSelMgr                As SldWorks.SelectionMgr
     Dim swFeat                  As SldWorks.Feature
     Dim swRip                   As SldWorks.RipFeatureData
     Dim vEdge                   As Variant
     Dim swEdge                  As SldWorks.Edge
     Dim swEnt                   As SldWorks.Entity
     Dim i                       As Long
     Dim lRipDirection           As Long
     Dim bRet                    As Boolean
     Dim longstatus As Long, longwarnings As Long

    Set swApp = Application.SldWorks
    lRipDirection = 64
    Set swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\box.sldprt", 1, 0, "", longstatus, longwarnings)
     swApp.ActivateDoc2 "box", False, longstatus
     Set swModel = swApp.ActiveDoc
     Set swSelMgr = swModel.SelectionManager
    bRet = swModel.Extension.SelectByID2("", "FACE", -5.66885410894997E-02, 2.99999999999159E-02, 2.00993374069753E-02, False, 1, Nothing, 0)
     swModel.InsertFeatureShell 0.01, False

    bRet = swModel.Extension.SelectByID2("", "EDGE", 4.41585455038194E-02, 1.51990980971277E-02, 4.59121462268968E-02, True, lRipDirection, Nothing, 0)
     swModel.InsertRip 0.0001

    bRet = swModel.Extension.SelectByID2("Rip1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
     Set swFeat = swSelMgr.GetSelectedObject6(1, -1)

    ' Get rip feature data
     Set swRip = swFeat.GetDefinition

     Debug.Print "Gap: " & swRip.Gap * 1000# & " mm"
    bRet = swRip.AccessSelections(swModel, Nothing)

    Debug.Print "Number of edges: " & swRip.GetEdgesCount
    swModel.ClearSelection2 (True)
    vEdge = swRip.Edges
    For i = 0 To UBound(vEdge)
        Set swEdge = vEdge(i)
         Set swEnt = swEdge
        Debug.Print "Direction of rip for edge (0=current, 1=other, 2=both): " & swRip.GetDirection(swEdge)
        bRet = swEnt.Select4(True, Nothing)
    Next i
    swRip.ReleaseSelectionAccess
End Sub
```
