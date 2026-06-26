---
title: "Change Active Tab in Manager Pane Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Active_Tab_in_Manager_Pane_Example_VBNET.htm"
---

# Change Active Tab in Manager Pane Example (VB.NET)

This example shows how to change the active tab in the Manager Pane.

```
'-----------------------------------------------------------------
' Preconditions:
' 1. Open an assembly and click the FeatureManager design tree tab
'    in the Manager Pane.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Ensures that the Manager Pane is visible.
' 2. Traverses the tabs in the Manager Pane:
'    a. Changes the active tab.
'    b. Fires a notification.
' 3. Examine the Immediate window and Manager Pane.
'-----------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics
Imports System.Collections

Partial Class SolidWorksMacro

    Public WithEvents swAssy As AssemblyDoc

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExtension As ModelDocExtension
        Dim swModelViewManager As ModelViewManager
        Dim tabs() As Object
        Dim nbrTabs As Integer
        Dim nbrTab As Integer
        Dim openAssy As Hashtable

        swModel = swApp.ActiveDoc
        swAssy = swModel
        swModelDocExtension = swModel.Extension

        'Set up events
        openAssy = New Hashtable
        AttachEventHandlers()

        swModelViewManager = swModel.ModelViewManager

        'Ensure that Manager Pane is visible
        swModelDocExtension.HideFeatureManager(False)

        'Get the tabs in the Manager Pane
        tabs = swModelViewManager.GetFeatureManagerTabs
        nbrTabs = UBound(tabs) + 1
        Debug.Print("Number of tabs in Manager Pane: " & nbrTabs)

        'Traverse the tabs in the Manager Pane and change the active tab
        For nbrTab = 0 To UBound(tabs)
            swModelViewManager.ActiveFeatureManagerTabIndex = nbrTab
        Next

        Debug.Print("")

        Debug.Print("FeatureManager design tree tab index: " & swModelViewManager.GetFeatureManagerTreeTabIndex)
        Debug.Print("PropertyManager tab index:            " & swModelViewManager.GetPropertyManagerTabIndex)
        Debug.Print("ConfigurationManager tab index:       " & swModelViewManager.GetConfigurationManagerTabIndex)
        Debug.Print("DimXpertManager tab index:            " & swModelViewManager.GetDimXpertManagerTabIndex)
        Debug.Print("DisplayManager tab index:             " & swModelViewManager.GetDisplayManagerTabIndex)

    End Sub

    Sub AttachEventHandlers()
        AttachSWEvents()
    End Sub

    Sub AttachSWEvents()
        AddHandler swAssy.FeatureManagerTabActivatedNotify, AddressOf Me.swAssy_FeatureManagerTabActivatedNotify
    End Sub

    Public Function swAssy_FeatureManagerTabActivatedNotify(ByVal commandIndex As Integer, ByVal commandTabName As String) As Integer
        Debug.Print("Activated tab " & commandIndex & " whose name is " & commandTabName)
    End Function

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
