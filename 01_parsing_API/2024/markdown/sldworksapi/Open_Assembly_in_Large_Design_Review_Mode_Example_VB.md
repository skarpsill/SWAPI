---
title: "Open an Assembly in Large Design Review Mode Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Open_Assembly_in_Large_Design_Review_Mode_Example_VB.htm"
---

# Open an Assembly in Large Design Review Mode Example (VBA)

This example shows how to open an assembly in Large Design Review mode.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly to open in Large Design Review mode
'    exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Click OK in the Large Design Review dialog.
' 2. Opens the assembly.
' 3. Creates a section view.
' 4. Creates four snapshots in the DisplayManager:
'    * Home
'    * ASnap
'    * Snap2
'    * Snap3
' 5. Click OK in the Name Snapshot dialog.
' 6. Selects and fully resolves a component.
' 7. Inspect the Immediate window for snapshot information and inspect
'    the graphics area.
'
' NOTE: Because the assembly is used elsewhere, do not save changes.
' ---------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks

Dim Part As SldWorks.AssemblyDoc

Dim snap As SldWorks.snapShot

Dim snaps As Variant

Dim snap1 As SldWorks.snapShot

Dim snap2 As SldWorks.snapShot

Dim snap3 As SldWorks.snapShot

Dim i As Long

Dim boolstatus As Boolean

Dim longstatus As Long, longwarnings As Long

Option Explicit
```

```vb
Sub main()

    Set swApp = _
     Application.SldWorks

    ' Open a large assembly in Large Design Review mode
     Dim large_assembly_document As String
     large_assembly_document = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\motor casing.sldasm"
     Set Part = swApp.OpenDoc6(large_assembly_document, swDocASSEMBLY, swOpenDocOptions_ViewOnly, "", longstatus, longwarnings)

    ' Wait for the FeatureManager design tree to synchronize
     sleep 5

    ' Create section view
     Dim sViewData As Object
     Set sViewData = Part.ModelViewManager.CreateSectionViewData()
     Set sViewData.FirstPlane = Nothing
     sViewData.FirstReverseDirection = False
     sViewData.FirstOffset = -0.00508
     sViewData.FirstRotationX = 0
     sViewData.FirstRotationY = 0
     sViewData.FirstColor = 16711680
     sViewData.ShowSectionCap = True
     sViewData.KeepCapColor = True
     Dim mvmgr As ModelViewManager
     Set mvmgr = Part.ModelViewManager
     boolstatus = mvmgr.CreateSectionView(sViewData)
     Part.ClearSelection2 True
     Part.ShowNamedView2 "*Front", 1
     Part.ShowNamedView2 "*Dimetric", 9

    ' Add a named snapshot
     Set snap1 = mvmgr.AddSnapShot("ASnap")
     ' Open dialog box to name the next snapshot
     Set snap2 = mvmgr.AddSnapShot("?")
     ' Add a snapshot with the next default name
     Set snap3 = mvmgr.AddSnapShot("")

    snap1.Comment = "<TS> This is a comment for ASnap."

    snaps = mvmgr.GetSnapShots

    For i = 0 To UBound(snaps)
         Set snap = snaps(i)
         snap.Activate
         Debug.Print "Snapshot name: " & snap.Name
         Debug.Print "      Comment: " & snap.Comment
         Debug.Print "       ViewID: " & snap.ViewId
     Next
```

```
   ' Selects a component
    boolstatus = Part.Extension.SelectByID2("motor casing-1@motor casing", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
```

```
   ' Fully resolve only the selected component
   Part.SelectiveOpen True, False
```

```vb
End Sub
 Sub sleep(PauseTime As Integer)
     Dim Start, TotalTime as Integer
     Start = Timer    ' Set start time
     Do While Timer < Start + PauseTime
         DoEvents    ' Yield to other processes
     Loop
 End Sub
```
