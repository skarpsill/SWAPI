---
title: "ModelDoc::EditRollback2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__EditRollback2.htm"
---

# ModelDoc::EditRollback2

This
method is obsolete and has been superseded by[ModelDoc2::EditRollback2](../ModelDoc2/ModelDoc2__EditRollback2.htm).

Description

This function rolls back the model to just
before the selected feature.

Syntax (OLE Automation)

retval = ModelDoc.EditRollback2 ( )

(Table)=========================================================

| Return: | (BOOL) retval | TRUE if rollback successful, FALSE otherwise |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->EditRollback2 ( &retval
)

(Table)=========================================================

| Output: | (VARIANT_BOOL) retval | TRUE if rollback successful, FALSE otherwise |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The selected feature,and those below it in the
FeatureManager design tree arekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}suppressed
and not accessible.

This routine is identical to ModelDoc::EditRollback.
The version number was incremented to allow VB applications to take advantage
of information not available inkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}PartDoc::EditRollback.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc\ModelDoc__EditRollback2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
