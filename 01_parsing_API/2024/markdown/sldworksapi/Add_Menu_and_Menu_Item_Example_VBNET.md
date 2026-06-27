---
title: "Add Menu and Menu Item Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Menu_and_Menu_Item_Example_VBNET.htm"
---

# Add Menu and Menu Item Example (VB.NET)

This example shows how to add a menu and menu item to a part.

```
'--------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the SOLIDWORKS API SDK add-in templates for your version
'    of Microsoft Visual Studio are installed.
' 2. In Microsoft Visual Studio, create a Visual Basic project using the
'    SwVBAddin template.
' 3. Name the project AddMenuItemVBNET.
' 4. Copy and paste SwAddin into SwAddin.vb of your project.
' 5. Click Project > AddMenuItemVBNET Properties > Debug.
' 6. Select Start external program and type the pathname of your
'    SOLIDWORKS executable.
' 7. Replace the images array elements with the pathnames of
'    your image files.
' 8. Press F5 to start debugging this add-in.
'
' Postconditions:
' 1. In SOLIDWORKS, click File > New > Part > OK.
' 2. Click Tools > MyMenu. Note the size of
'    the MyMenuItem button.
' 3. Click MyMenuItem and click OK to close the message box.
' 4. Exit SOLIDWORKS.
' 5. Change the size of the text and other items on your computer.
'    For example, in Windows 7:
'    a. Click Start > Control Panel > Appearance and
'       Personalization > Display.
'    b. Select a different size.
'    c. Click Apply.
'    d. Click Log off now.
'    e. Log back in.
' 6. Start SOLIDWORKS.
' 7. Repeat steps 1 and 2.
'---------------------------------------------------------------------------
'SwAddin
Imports System
Imports System.Collections
Imports System.Reflection
Imports System.Runtime.InteropServices
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports SolidWorks.Interop.swpublished
Imports SolidWorksTools
Imports SolidWorksTools.File
Imports System.Windows.Forms
Imports System.Collections.Generic
Imports System.Diagnostics

<Guid("2b89b82f-2984-439a-a818-3c79180e7916")> _
    <ComVisible(True)> _
    <SwAddin( _
        Description:="AddMenuItemVBNET description", _
        Title:="AddMenuItemVBNET", _
        LoadAtStartup:=True _
        )> _
Public Class SwAddin
    Implements SolidWorks.Interop.swpublished.SwAddin

#Region "Local Variables"
    Dim WithEvents iSwApp As SldWorks
    Dim addinID As Integer
    Dim openDocs As Hashtable
    Dim SwEventPtr As SldWorks

    ' Public properties
    ReadOnly Property SwApp() As SldWorks
        Get
            Return iSwApp
        End Get
    End Property

    ReadOnly Property OpenDocumentsTable() As Hashtable
        Get
            Return openDocs
        End Get
    End Property
#End Region

#Region "SolidWorks Registration"

    <ComRegisterFunction()> Public Shared Sub RegisterFunction(ByVal t As Type)

        ' Get Custom Attribute: SwAddinAttribute
        Dim attributes() As Object
        Dim SWattr As SwAddinAttribute = Nothing

        attributes = System.Attribute.GetCustomAttributes(GetType(SwAddin), GetType(SwAddinAttribute))

        If attributes.Length > 0 Then
            SWattr = DirectCast(attributes(0), SwAddinAttribute)
        End If
        Try
            Dim hklm As Microsoft.Win32.RegistryKey = Microsoft.Win32.Registry.LocalMachine
            Dim hkcu As Microsoft.Win32.RegistryKey = Microsoft.Win32.Registry.CurrentUser

            Dim keyname As String = "SOFTWARE\SolidWorks\Addins\{" + t.GUID.ToString() + "}"
            Dim addinkey As Microsoft.Win32.RegistryKey = hklm.CreateSubKey(keyname)
            addinkey.SetValue(Nothing, 0)
            addinkey.SetValue("Description", SWattr.Description)
            addinkey.SetValue("Title", SWattr.Title)

            keyname = "Software\SolidWorks\AddInsStartup\{" + t.GUID.ToString() + "}"
            addinkey = hkcu.CreateSubKey(keyname)
            addinkey.SetValue(Nothing, SWattr.LoadAtStartup, Microsoft.Win32.RegistryValueKind.DWord)
        Catch nl As System.NullReferenceException
            Console.WriteLine("There was a problem registering this dll: SWattr is null.\n " & nl.Message)
            System.Windows.Forms.MessageBox.Show("There was a problem registering this dll: SWattr is null.\n" & nl.Message)
        Catch e As System.Exception
            Console.WriteLine("There was a problem registering this dll: " & e.Message)
            System.Windows.Forms.MessageBox.Show("There was a problem registering this dll: " & e.Message)
        End Try
    End Sub

    <ComUnregisterFunction()> Public Shared Sub UnregisterFunction(ByVal t As Type)
        Try
            Dim hklm As Microsoft.Win32.RegistryKey = Microsoft.Win32.Registry.LocalMachine
            Dim hkcu As Microsoft.Win32.RegistryKey = Microsoft.Win32.Registry.CurrentUser

            Dim keyname As String = "SOFTWARE\SolidWorks\Addins\{" + t.GUID.ToString() + "}"
            hklm.DeleteSubKey(keyname)

            keyname = "Software\SolidWorks\AddInsStartup\{" + t.GUID.ToString() + "}"
            hkcu.DeleteSubKey(keyname)
        Catch nl As System.NullReferenceException
            Console.WriteLine("There was a problem unregistering this dll: SWattr is null.\n " & nl.Message)
            System.Windows.Forms.MessageBox.Show("There was a problem unregistering this dll: SWattr is null.\n" & nl.Message)
        Catch e As System.Exception
            Console.WriteLine("There was a problem unregistering this dll: " & e.Message)
            System.Windows.Forms.MessageBox.Show("There was a problem unregistering this dll: " & e.Message)
        End Try

    End Sub

#End Region

#Region "ISwAddin Implementation"

    Function ConnectToSW(ByVal ThisSW As Object, ByVal Cookie As Integer) As Boolean Implements SolidWorks.Interop.swpublished.SwAddin.ConnectToSW
        iSwApp = ThisSW
        addinID = Cookie

        ' Set up callbacks
        iSwApp.SetAddinCallbackInfo2(0, Me, addinID)

        ' Set up the menu item
        AddMenuItem()

        ' Set up the Event Handlers
        SwEventPtr = iSwApp
        openDocs = New Hashtable
        AttachEventHandlers()

        ConnectToSW = True
    End Function

    Function DisconnectFromSW() As Boolean Implements SolidWorks.Interop.swpublished.SwAddin.DisconnectFromSW

        DetachEventHandlers()

        System.Runtime.InteropServices.Marshal.ReleaseComObject(iSwApp)
        iSwApp = Nothing
        'The add-in must call GC.Collect() here to retrieve all managed code pointers
        GC.Collect()
        GC.WaitForPendingFinalizers()

        GC.Collect()
        GC.WaitForPendingFinalizers()

        DisconnectFromSW = True
    End Function
#End Region

#Region "UI Methods"
    ' Add menu and menu item
    Public Sub AddMenuItem()
        Dim thisAssembly1 As Assembly
        Dim images As String() = New String(2) {}
        Dim menuId As Integer = 0

        thisAssembly1 = System.Reflection.Assembly.GetAssembly(Me.[GetType]())

        images(0) = "Pathname_to_menu_item_nxn_image"
        images(1) = "Pathname_to_menu_item_nnxnn_image"
        images(2) = "Pathname_to_menu_item_nnnxnnn_image"

        menuId = SwApp.AddMenu(swDocumentTypes_e.swDocPART, "MyMenu", 0)
        menuId = iSwApp.AddMenuItem5(swDocumentTypes_e.swDocPART, addinID, "MyMenuItem@MyMenu", 0, "MyMenuCallback", "MyMenuEnableMethod", "My menu item", images)

    End Sub

    Function CompareIDs(ByVal storedIDs() As Integer, ByVal addinIDs() As Integer) As Boolean

        Dim storeList As New List(Of Integer)(storedIDs)
        Dim addinList As New List(Of Integer)(addinIDs)

        addinList.Sort()
        storeList.Sort()

        If Not addinList.Count = storeList.Count Then

            Return False
        Else

            For i As Integer = 0 To addinList.Count - 1
                If Not addinList(i) = storeList(i) Then

                    Return False
                End If
            Next
        End If

        Return True
    End Function
#End Region

#Region "UI callbacks"
    Public Sub MyMenuCallback()
        MessageBox.Show("Callback function called.")
    End Sub

#End Region

#Region "Event Methods"
    Sub AttachEventHandlers()
        AttachSWEvents()

        'Listen for events on all currently open documents
        AttachEventsToAllDocuments()
    End Sub

    Sub DetachEventHandlers()
        DetachSWEvents()

        'Close events on all currently open documents
        Dim docHandler As DocumentEventHandler
        Dim key As ModelDoc2
        Dim numKeys As Integer
        numKeys = openDocs.Count
        If numKeys > 0 Then
            Dim keys() As Object = New Object(numKeys - 1) {}

            'Remove all document event handlers
            openDocs.Keys.CopyTo(keys, 0)
            For Each key In keys
                docHandler = openDocs.Item(key)
                'Remove the pair from the hash
                docHandler.DetachEventHandlers()
                docHandler = Nothing
                key = Nothing
            Next
        End If
    End Sub

    Sub AttachSWEvents()
        Try
            AddHandler iSwApp.ActiveDocChangeNotify, AddressOf Me.SldWorks_ActiveDocChangeNotify
            AddHandler iSwApp.DocumentLoadNotify2, AddressOf Me.SldWorks_DocumentLoadNotify2
            AddHandler iSwApp.FileNewNotify2, AddressOf Me.SldWorks_FileNewNotify2
            AddHandler iSwApp.ActiveModelDocChangeNotify, AddressOf Me.SldWorks_ActiveModelDocChangeNotify
            AddHandler iSwApp.FileOpenPostNotify, AddressOf Me.SldWorks_FileOpenPostNotify
        Catch e As Exception
            Console.WriteLine(e.Message)
        End Try
    End Sub

    Sub DetachSWEvents()
        Try
            RemoveHandler iSwApp.ActiveDocChangeNotify, AddressOf Me.SldWorks_ActiveDocChangeNotify
            RemoveHandler iSwApp.DocumentLoadNotify2, AddressOf Me.SldWorks_DocumentLoadNotify2
            RemoveHandler iSwApp.FileNewNotify2, AddressOf Me.SldWorks_FileNewNotify2
            RemoveHandler iSwApp.ActiveModelDocChangeNotify, AddressOf Me.SldWorks_ActiveModelDocChangeNotify
            RemoveHandler iSwApp.FileOpenPostNotify, AddressOf Me.SldWorks_FileOpenPostNotify
        Catch e As Exception
            Console.WriteLine(e.Message)
        End Try
    End Sub

    Sub AttachEventsToAllDocuments()
        Dim modDoc As ModelDoc2
        modDoc = iSwApp.GetFirstDocument()
        While Not modDoc Is Nothing
            If Not openDocs.Contains(modDoc) Then
                AttachModelDocEventHandler(modDoc)
            Else
                Dim docHandler As DocumentEventHandler = openDocs(modDoc)
                If Not docHandler Is Nothing Then
                    docHandler.ConnectModelViews()
                End If
            End If
            modDoc = modDoc.GetNext()
        End While
    End Sub

    Function AttachModelDocEventHandler(ByVal modDoc As ModelDoc2) As Boolean
        If modDoc Is Nothing Then
            Return False
        End If
        Dim docHandler As DocumentEventHandler = Nothing

        If Not openDocs.Contains(modDoc) Then
            Select Case modDoc.GetType
                Case swDocumentTypes_e.swDocPART
                    docHandler = New PartEventHandler()
                Case swDocumentTypes_e.swDocASSEMBLY
                    docHandler = New AssemblyEventHandler()
                Case swDocumentTypes_e.swDocDRAWING
                    docHandler = New DrawingEventHandler()
            End Select

            docHandler.Init(iSwApp, Me, modDoc)
            docHandler.AttachEventHandlers()
            openDocs.Add(modDoc, docHandler)
        End If
    End Function

    Sub DetachModelEventHandler(ByVal modDoc As ModelDoc2)
        Dim docHandler As DocumentEventHandler
        docHandler = openDocs.Item(modDoc)
        openDocs.Remove(modDoc)
        modDoc = Nothing
        docHandler = Nothing
    End Sub
#End Region

#Region "Event Handlers"
    Function SldWorks_ActiveDocChangeNotify() As Integer
        ' TODO: Add your implementation here
    End Function

    Function SldWorks_DocumentLoadNotify2(ByVal docTitle As String, ByVal docPath As String) As Integer
        ' TODO: Add your implementation here
    End Function

    Function SldWorks_FileNewNotify2(ByVal newDoc As Object, ByVal doctype As Integer, ByVal templateName As String) As Integer
        AttachEventsToAllDocuments()
    End Function

    Function SldWorks_ActiveModelDocChangeNotify() As Integer
        ' TODO: Add your implementation here
    End Function

    Function SldWorks_FileOpenPostNotify(ByVal FileName As String) As Integer
        AttachEventsToAllDocuments()
    End Function

#End Region

End Class
```
