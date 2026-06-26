---
title: "Get Comments in Comments Folder Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Comments_in_Comments_Folder_Example_VBNET.htm"
---

# Get Comments in Comments Folder Example (VB.NET)

This example shows how to add and get the comments in a Comments folder.

```
'---------------------------------------------
' Preconditions:
' 1. Verify that the specified model document
'    to open exits.
' 2. Open Immediate window.
'
' Postconditions:
' 1. Examine the FeatureManager design tree
'    to verify that the Comments folder is not
'    shown, then press F5.
' 2. Adds a comment to the Comments folder
'    and updates the FeatureManager design
'    tree.
' 3. Examine the FeatureManager design tree
'    to verify that the Comments folder is
'    shown, then press F5.
' 4. Prints the number of comments, name of the
'    the comments, and text of the comments
'    in the Comments folder to the Immediate
'    window. Examine the Immediate window.
'
' NOTE: Because this model document is used
' elsewhere, do not save changes.
'-------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModelDoc As ModelDoc2
        Dim swFeat As Feature
        Dim swFeatMgr As FeatureManager
        Dim swCommentFolder As CommentFolder
        Dim swComment As Comment
        Dim nbrComments As Integer
        Dim sFeatType As String
        Dim vComments As Object
        Dim fileName As String
        Dim errors As Integer
        Dim warnings As Integer
        Dim i As Long

        ' Open part document
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\2012-sm.sldprt"
        swModelDoc = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

        ' Traverse the FeatureManager design tree for Comments folder

        ' Get first feature in FeatureManager design tree
        swFeat = swModelDoc.FirstFeature
        swFeatMgr = swModelDoc.FeatureManager

        Stop
        ' Examine FeatureManager design tree to verify that
        ' the the Comments folder is not shown; press F5

        Do While Not swFeat Is Nothing
            sFeatType = swFeat.GetTypeName

            ' If Comments folder, add a comment
            If sFeatType = "CommentsFolder" Then
                swCommentFolder = swFeat.GetSpecificFeature2

                ' Add comment and update FeatureManager design tree
                ' so that Comments folder is shown
                swComment = swCommentFolder.AddComment("First comment in comment folder.")
                swFeatMgr.UpdateFeatureTree()

                Stop
                ' Locate Comments folder in FeatureManager design; press F5

                ' Get number of comments in Comment folder
                nbrComments = swCommentFolder.GetCommentCount
                Debug.Print("Number of comments in Comments folder         = " & nbrComments)

                vComments = swCommentFolder.GetComments
                For i = 0 To (nbrComments - 1)
                    swComment = vComments(i)
                    Debug.Print("Name of comment in FeatureManager design tree = " & swComment.Name)
                    Debug.Print("Text of comment                               = " & swComment.Text)
                    Debug.Print("")
                Next i
            End If

            ' Get next feature in FeatureManager design tree
            swFeat = swFeat.GetNextFeature

        Loop

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
