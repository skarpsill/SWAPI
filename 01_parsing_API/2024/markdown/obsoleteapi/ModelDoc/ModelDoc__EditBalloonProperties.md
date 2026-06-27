---
title: "ModelDoc::EditBalloonProperties"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__EditBalloonProperties.htm"
---

# ModelDoc::EditBalloonProperties

This
method is obsolete and has been superseded by[ModelDoc2::EditBalloonProperties](../ModelDoc2/ModelDoc2__EditBalloonProperties.htm).

Description

This method edits the selected balloon's properties.

Syntax (OLE Automation)

retval = ModelDoc.EditBalloonProperties ( style,
size, upperTextStyle, upperText, lowerTextStyle, lowerText )

(Table)=========================================================

| Input: | (long) style | Style of balloon you wish to use as defined in
swBalloonStyle_e |
| --- | --- | --- |
| Input: | (long) size | Balloon size you wish to use as defined in swBalloonFit_e |
| Input: | (long) upperTextStyle | Upper text style as defined in swDetailingNoteTextContent_e |
| Input: | (BSTR) upperText | Text string for the upper text in this balloon |
| Input: | (long) lowerTextStyle | Lower text style as defined in swDetailingNoteTextContent_e |
| Input: | (BSTR) lowerText | Text string for the lower text in this balloon |
| Return: | (LPDISPATCH) retval | Pointer to the balloon that is being edited |

Syntax (COM)

status = ModelDoc->EditBalloonProperties ( style,
size, upperTextStyle, upperText, lowerTextStyle, lowerText, &retval
)

(Table)=========================================================

| Input: | (long) style | Style of balloon you wish to use as defined in
swBalloonStyle_e |
| --- | --- | --- |
| Input: | (long) size | Balloon size you wish to use as defined in swBalloonFit_e |
| Input: | (long) upperTextStyle | Upper text style as defined in swDetailingNoteTextContent_e |
| Input: | (BSTR) upperText | Text string for the upper text in this balloon. |
| Input: | (long) lowerTextStyle | Lower text style as defined in swDetailingNoteTextContent_e |
| Input: | (BSTR) lowerText | Text string for the lower text in this balloon |
| Output: | (LPDISPATCH) retval | Pointer to the balloon that is being edited |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes2001$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\ModelDoc\ModelDoc__EditBalloonProperties.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\obsoleteapi\ModelDoc\ModelDoc__EditBalloonProperties.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
