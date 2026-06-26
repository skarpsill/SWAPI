---
title: "Copy and Paste Appearances Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Copy_and_Paste_Appearances_Example_VB.htm"
---

# Copy and Paste Appearances Example (VBA)

This example shows how to copy an appearance from one entity and apply it to other entities.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a part or assembly that has appearances.
 ' 2. Press F5.
 ' 3. At the breakpoints, follow the instructions in the Immediate window.
 ' 4. Repeat steps 2 and 3 until the macro is finished.
 '
 ' Postconditions: None
 ' ---------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim boolstatus As Boolean
Option Explicit
Sub main()
    Set swApp = Application.SldWorks
     Set Part = swApp.ActiveDoc

    Dim pEnt As Object
     Dim selMgr As SelectionMgr
     Set selMgr = Part.SelectionManager

    Debug.Print "Select a face, feature, body, component, or part that has an appearance."
     Stop

    Set pEnt = selMgr.GetSelectedObject6(1, -1)

     ' Copy appearance to the clipboard
     boolstatus = swApp.CopyAppearance(pEnt)

    If Part.GetType = swDocPART Then

        Debug.Print "Select a face to which to apply the copied appearance."
         Stop

        Set pEnt = selMgr.GetSelectedObject6(1, -1)
         boolstatus = swApp.PasteAppearance(pEnt, swAppearanceTargetFace)

        Debug.Print "Select a face to whose feature is applied the copied appearance."
         Stop

        Set pEnt = selMgr.GetSelectedObject6(1, -1)
         boolstatus = swApp.PasteAppearance(pEnt, swAppearanceTargetFeature)

        Debug.Print "Select a face to whose body is applied the copied appearance."
         Stop

        Set pEnt = selMgr.GetSelectedObject6(1, -1)
         boolstatus = swApp.PasteAppearance(pEnt, swAppearanceTargetBody)

        Debug.Print "Select a face to whose part is applied the copied appearance."
         Stop

        Set pEnt = selMgr.GetSelectedObject6(1, -1)
         boolstatus = swApp.PasteAppearance(pEnt, swAppearanceTargetPart)

        Debug.Print "Select a face. All appearances in the model that match that of the selected face are changed to the copied appearance."
         Stop

        Set pEnt = selMgr.GetSelectedObject6(1, -1)
         boolstatus = swApp.PasteAppearance(pEnt, swAppearanceTargetAppearanceFilter)

        Debug.Print "Select a feature to which to apply the copied appearance."
         Stop

        Set pEnt = selMgr.GetSelectedObject6(1, -1)
         boolstatus = swApp.PasteAppearance(pEnt, swAppearanceTargetAppearanceFilter) ' The second parameter is ignored.

        Debug.Print "Select a body to which to apply the copied appearance."
         Stop

        Set pEnt = selMgr.GetSelectedObject6(1, -1)
         boolstatus = swApp.PasteAppearance(pEnt, swAppearanceTargetAppearanceFilter) ' The second parameter is ignored.

        Debug.Print "No input entity. Preselect an entity in the graphics area to whose body is applied the copied appearance."
         Stop

        boolstatus = swApp.PasteAppearance(Nothing, swAppearanceTargetBody)

    ElseIf Part.GetType = swDocASSEMBLY Then

        Debug.Print "Select a part to which to apply the copied appearance."
         Stop

        Set pEnt = selMgr.GetSelectedObject6(1, -1)
         boolstatus = swApp.PasteAppearance(pEnt, swAppearanceTargetAppearanceFilter) ' The second parameter is ignored.

        Debug.Print "Select a face to whose component is applied the copied appearance."
         Stop

        Set pEnt = selMgr.GetSelectedObject6(1, -1)
         boolstatus = swApp.PasteAppearance(pEnt, swAppearanceTargetComponent)

        Debug.Print "Select a face to whose body is applied the copied appearance."
         Stop

        Set pEnt = selMgr.GetSelectedObject6(1, -1)
         boolstatus = swApp.PasteAppearance(pEnt, swAppearanceTargetBody)

        Debug.Print "Select a face to whose feature is applied the copied appearance."
         Stop

        Set pEnt = selMgr.GetSelectedObject6(1, -1)
         boolstatus = swApp.PasteAppearance(pEnt, swAppearanceTargetFeature)

        Debug.Print "Select a face to which is applied the copied appearance."
         Stop

        Set pEnt = selMgr.GetSelectedObject6(1, -1)
         boolstatus = swApp.PasteAppearance(pEnt, swAppearanceTargetFace)

        Debug.Print "Select a face to whose part is applied the copied appearance."
         Stop

        Set pEnt = selMgr.GetSelectedObject6(1, -1)
         boolstatus = swApp.PasteAppearance(pEnt, swAppearanceTargetPart)
     End If
End Sub
```
