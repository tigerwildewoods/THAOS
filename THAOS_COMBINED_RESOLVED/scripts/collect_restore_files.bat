@echo off
set TARGET=THAOS_RESTORE_EXPORT
if not exist %TARGET% mkdir %TARGET%
for %%F in (
 data\THAOS_MASTER_COMBINED_DEDUPE.txt
 data\THAOS_CATEGORIZED.txt
 data\THAOS_CATEGORIZED_REFERENCE.txt
 data\THAOS_PIPELINE_REFERENCE.txt
 data\THAOS_SELF_RESTORE_TOOL.txt
 data\THAOS_RESTORE_SCRIPT.txt
 data\THAOS_AUTORUN_RESTORE.txt
 data\THAOS_WORLDSTATE.txt
) do (
 if exist "%%F" copy "%%F" "%TARGET%"
)
echo Collected restore files.
pause
