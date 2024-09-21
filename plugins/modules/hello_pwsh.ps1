#!/usr/bin/env pwsh

Function Invoke-AnsibleModule([hashtable]$module_args) {
    $GREET_STRING_SPEC = "Hello from Powershell, {0}!"

    $check_mode = $module_args._ansible_check_mode
    $greet_name = $module_args.greet_name.ToUpper()

    $greeting = $GREET_STRING_SPEC -f $greet_name

    try {
        if ($check_mode) {
            $obj = @{changed = $false; result = "Would greet with [{0}]" -f $greeting }
        }
        else {
            $obj = @{changed = $true; result = $greeting }
        }

        Exit-Json $obj
    }
    catch {
        $obj = @{changed = $false; result = "Failed greet with [{0}]" -f $greeting }
        Fail-Json $obj $_.Exception.Message
    }
}


try {
    $ansible_module_json_args = '<<INCLUDE_ANSIBLE_MODULE_JSON_ARGS>>'
    $module_args = $ansible_module_json_args | ConvertFrom-Json -AsHashtable
    Invoke-AnsibleModule $module_args
}
catch {
    Fail-Json $null $_.Exception.Message
}
