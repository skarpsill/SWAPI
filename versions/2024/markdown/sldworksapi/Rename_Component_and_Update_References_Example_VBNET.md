---
title: "Rename Component and Update References Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Rename_Component_and_Update_References_Example_VBNET.htm"
---

# Rename Component and Update References Example (VB.NET)

This example shows how to rename a component and update its references.

```
'----------------------------------------------------------------------
' Preconditions:
' 1. Copy public_documents\samples\tutorial\EDraw\claw to c:\test\claw.
' 2. Open c:\test\claw\claw-mechanism.sldasm and save the file as
'    claw-mechanism-copy.sldasm.
' 3. Close claw-mechanism-copy.sldasm and reopen claw-mechanism.sldasm.
' 4. Open the Immediate window.
'
' Postconditions:
' 1. Renames the center component to centerXXX.
' 2. Fires the RenameItemNotify event.
' 3. Saves the assembly.
' 4. Fires the RenamedDocumentNotify event.
' 5. Updates references.
' 6. Examine the FeatureManager design tree and Immediate window.
' 7. Close claw-mechanism.sldasm and open
'    c:\test\claw\claw-mechanism-copy.sldasm to verify that the
'    center component was renamed to centerXXX.
'---------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics
Imports System.Collections

Partial Class SolidWorksMacro

    Public WithEvents assy As AssemblyDoc

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swAssy As AssemblyDoc
        Dim openAssembly As Hashtable
        Dim errors As Integer
        Dim warnings As Integer
        Dim status As Boolean

        swAssy = swApp.ActiveDoc

        'Set up event
        assy = swAssy
        openAssembly = New Hashtable
        AttachEventHandlers()

        swModel = swAssy
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("center-1@claw-mechanism", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
        errors = swModelDocExt.RenameDocument("centerXXX")
        swModelDocExt.Rebuild(swRebuildOptions_e.swRebuildAll)
        status = swModel.Save3(swSaveAsOptions_e.swSaveAsOptions_Silent + swSaveAsOptions_e.swSaveAsOptions_SaveReferenced, errors, warnings)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

    Sub AttachEventHandlers()
        AttachSWEvents()
    End Sub

    Sub AttachSWEvents()
        If Not assy Is Nothing Then
            AddHandler assy.RenameItemNotify, AddressOf Me.assy_RenameItemNotify
            AddHandler assy.RenamedDocumentNotify, AddressOf Me.assy_RenamedDocumentNotify
        End If

    End Sub

    'Fire notification when item is renamed
    Public Function assy_RenameItemNotify(ByVal entType As Integer, ByVal oldName As String, ByVal newName As String) As Integer
        Debug.Print("RenameItemNotify fired")
    End Function

    'Fire notification for Rename Documents dialog
    Public Function assy_RenamedDocumentNotify(ByRef swObj As Object) As Integer
        Dim swRenamedDocumentReferences As RenamedDocumentReferences
        Dim searchPaths As Object
        Dim pathNames As Object
        Dim i As Integer
        Dim nbr As Integer

        swRenamedDocumentReferences = swObj

        swRenamedDocumentReferences.UpdateWhereUsedReferences = True
        swRenamedDocumentReferences.IncludeFileLocations = True

        searchPaths = swRenamedDocumentReferences.GetSearchPath
        nbr = UBound(searchPaths)
        Debug.Print("Search paths:")
        For i = 0 To nbr
            Debug.Print(" " & searchPaths(i))
        Next i

        swRenamedDocumentReferences.Search()

        pathNames = swRenamedDocumentReferences.ReferencesArray
        nbr = UBound(pathNames)
        Debug.Print("References:")
        For i = 0 To nbr
            Debug.Print(" " & pathNames(i))
        Next i

        swRenamedDocumentReferences.CompletionAction = swRenamedDocumentFinalAction_e.swRenamedDocumentFinalAction_Ok

        Debug.Print("RenamedDocumentNotify fired")

    End Function

End Class
```
