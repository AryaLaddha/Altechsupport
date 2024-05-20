import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

const Navbar = () => {
    return (
        <nav class="flex items-center justify-between flex-wrap bg-[#1e3a5f] p-6">
            <div class="flex items-center flex-shrink-0 text-white mr-6">
                <span class="font-semibold text-xl tracking-tight"><Link to="/">ALTECH</Link></span>
            </div>
            <div class="w-full block flex-grow lg:flex lg:items-center lg:w-auto">
                <div class="text-sm lg:flex-grow">
                    <a href="#responsive-header" class="block mt-4 lg:inline-block lg:mt-0 text-teal-200 hover:text-white mr-4">
                    Docs
                    </a>
                    <a href="#responsive-header" class="block mt-4 lg:inline-block lg:mt-0 text-teal-200 hover:text-white mr-4">
                    Examples
                    </a>
                    <a href="#responsive-header" class="block mt-4 lg:inline-block lg:mt-0 text-teal-200 hover:text-white">
                    Blog
                    </a>
                </div>
                <div className='flex space-x-4 items-center lg:justify-center text-sm'>
                    <div>
                        <Link to="/login" className="block mt-4 lg:inline-block lg:mt-0 text-teal-200 hover:text-white">
                        Login
                        </Link>
                    </div>
                    <div>
                        <Link to="/register" class="inline-block text-sm px-4 py-2 leading-none border rounded text-white border-white hover:border-transparent hover:text-[#1e3a5f] hover:bg-white mt-4 lg:mt-0">Register</Link>
                    </div>
                </div>
            </div>
        </nav>
    )
}

export default Navbar