---
title: "Recognizing Features Interactively (VBA)"
project: ""
interface: ""
member: ""
kind: "topic"
source: "fworksapi/Recognizing_Features_Interactively.htm"
---

# Recognizing Features Interactively (VBA)

This sample application illustrates recognizing a feature interactively
in a SOLIDWORKS part document, and then creating that feature.

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swApp As Object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
sample As Object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
Part As Object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
boolstatus As Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
str As String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swApp.SetUserPreferenceIntegerValue
swAutoSaveInterval, 0

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
sample = swApp.GetAddInObject("FeatureWorks.FeatureWorksApp")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
varOut As Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
var1 As Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
Part = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
Part = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}boolstatus
= Part.Extension.SelectByID("", "FACE", 0.1165311335518,
-0.006695921966639, 0.03257260156937, False, 0, Nothing)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
InterOption As Integer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}str
= "Fillet" 'Option to recognize interactive fillet

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}InterOption
= fwChainFeatures 'Turn on the chaining option.

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}varOut
= sample.RecognizeFeatureInteractive(str,
InterOption)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
(False = varOut) Then MsgBox ("ERROR")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}createOption
= fwAllowFailFeatureCreation 'Option to allow creation of features with
rebuild errors

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}var1
= sample.CreateFeatures(createOption)kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

If (False = var1) Then MsgBox ("ERROR")

End Sub

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

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
