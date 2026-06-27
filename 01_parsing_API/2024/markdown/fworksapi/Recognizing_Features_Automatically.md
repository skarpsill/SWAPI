---
title: "Recognizing Features Automatically (VBA)"
project: ""
interface: ""
member: ""
kind: "topic"
source: "fworksapi/Recognizing_Features_Automatically.htm"
---

# Recognizing Features Automatically (VBA)

This sample application illustrates recognizing features automatically
in a SOLIDWORKS part document, and then creating those features.

Sub main()

Dim swApp As Object

Dim sample As Object

Dim Part As Object

Dim boolstatus As Boolean

Dim inp As Boolean

Dim str1 As String

' Get the SOLIDWORKS object

Set swApp = CreateObject("SldWorks.Application")

' CLSID of FeatureWorks : 16B0AE50-0817-11d7-A7F8-0006299907FB

' Get the FeatureWorks object

Set sample = swApp.GetAddInObject("FeatureWorks.FeatureWorksApp")

Dim varOut As Variant

Dim var1 As Boolean

Dim unused As Integer

Dim options As Long

unused = 0

Dim str1 As String

' Get the SOLIDWORKS part document

Set Part = swApp.ActiveDoc

' Select the faces to fillet

boolstatus = Part.Extension.SelectByID("", "FACE",
0.1023433561252, 0.06999999999994, 0.05499949188089, False, 8, Nothing)

' Turn on the specified automatic feature recognition
options

option = fwChamfils + fwExtrudeOption

varOut = sample.RecognizeFeatureAutomatic(option
)

' Create the recognized features

createOption = fwAllowFailFeatureCreation 'Option to allow
creation of features with reubild errors

var1 = sample.CreateFeatures(createOption)

End Sub

kadov_tag{{<implicit_p>}}

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="FWApplicationBasics$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="" >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\fworksapi\GettingStarted\Example_Recognizing_Features_Automatically.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>

Metadata type="DesignerControl" endspan
