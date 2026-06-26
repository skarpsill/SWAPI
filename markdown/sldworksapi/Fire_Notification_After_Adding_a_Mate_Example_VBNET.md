---
title: "Fire Notification After Adding a Mate Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Notification_After_Adding_a_Mate_Example_VBNET.htm"
---

# Fire Notification After Adding a Mate Example (VB.NET)

This example shows how to fire a post-notify event when adding mates.

```
'-----------------------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly to open exists.
' 2. Click Tools > Options > clear the Stop VSTA debugger
'    on macro exit check box if it is selected.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Opens the assembly.
' 2. Interactively add a mate between two entities
'    (Click Insert > Mate). For example, add a lock mate
'    between the toaster base and the cup.
' 3. Adds a mate between the selected entities.
' 4. Examine the Immediate window.
' 5. Click Debug > Stop Debugging in SOLIDWORKS Visual
'    Studio Tools for Applications.
' 6. Click Tools > Options > Stop VSTA debugger on macro exit
'    check box in SOLIDWORKS.
'
' NOTE: Because this assembly is used elsewhere, do not save
' changes.
'-----------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics
Imports System.Collections

Partial Class SolidWorksMacro

    Public WithEvents swAssemblyDoc As AssemblyDoc

    Public Sub Main()
        Dim swModel As ModelDoc2

        Dim errorstatus As Long, warningstatus As Long
        Dim openAssem As Hashtable

        ' Open assembly document
        swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\tutorial\api\toaster_scene.sldasm", swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errorstatus, warningstatus)
        swModel = swApp.ActiveDoc

        ' Set up event
        swAssemblyDoc = swModel
        openAssem = New Hashtable
        AttachEventHandlers()

    End Sub

    Sub AttachEventHandlers()
        AttachSWEvents()
    End Sub

    Sub AttachSWEvents()
        AddHandler swAssemblyDoc.AddMatePostNotify2, AddressOf Me.swAssemblyDoc_AddMatePostNotify2
    End Sub

    Private Function swAssemblyDoc_AddMatePostNotify2(ByRef mates As Object) As Integer
        Debug.Print("One or more mates were added to the assembly.")
    End Function

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
